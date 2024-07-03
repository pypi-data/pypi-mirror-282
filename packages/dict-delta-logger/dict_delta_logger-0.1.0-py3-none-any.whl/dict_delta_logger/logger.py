"""
Author: Yu-Cheng Huang
Date: 2024/07/03

This module provides the DeltaLogger class, which is used to log messages to JSON files. The logs are rotated when they reach a specified size, and a maximum number of log files can be maintained.
"""

import os
import json
import logging
from typing import Dict, Any
from pathlib import Path


class DictDeltaLogger:
    def __init__(self, log_name: str, log_dir: str = ".", max_file_size: int = 200 * 1024 * 1024, max_files: int = -1):
        """
        Initialize the DeltaLogger.

        :param log_name: The base name for log files.
        :param log_dir: The directory where log files will be stored.
        :param max_file_size: The maximum size of each log file in bytes.
        :param max_files: The maximum number of log files to maintain.
        """
        self.log_name = log_name
        self.log_dir = Path(log_dir)
        self.max_file_size = max_file_size
        self.max_files = max_files
        self.current_log_index = 0

        # Ensure the log directory exists
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.current_log_path = self._get_new_log_path()

        if max_files == 0:
            logging.warning("Logging is disabled as max_files is set to 0.")
        
        self._setup_logger()

    def _setup_logger(self):
        """
        Set up the logger.
        """
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(logging.DEBUG)
        
        if self.max_files == 0:
            return

        handler = logging.StreamHandler()  # To capture log messages without file handler
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(handler)

    def _get_new_log_path(self):
        """
        Get a new log file path with an incremented index.
        """
        self.current_log_index += 1
        return self.log_dir / f"log_{self.log_name}_{self.current_log_index:010d}.json"

    def _rotate_logs(self):
        """
        Rotate the logs by creating a new log file path.
        """
        if self.max_files == 0:
            return

        self.current_log_path = self._get_new_log_path()

        if self.max_files > 0:
            self._maintain_max_files()

    def _maintain_max_files(self):
        """
        Maintain the maximum number of log files by removing the oldest ones.
        """
        log_files = sorted(self.log_dir.glob(f"log_{self.log_name}_*.json"))
        while len(log_files) > self.max_files:
            oldest_log_file = log_files.pop(0)
            oldest_log_file.unlink()
            self.logger.info(f"Removed old log file: {oldest_log_file}")

    def log(self, message: Dict[str, Any]):
        """
        Log a message after validating it with the Pydantic model.

        :param message: The log message as a dictionary.
        """
        if self.max_files == 0:
            return

        if os.path.exists(self.current_log_path) and os.path.getsize(self.current_log_path) >= self.max_file_size:
            self._rotate_logs()

        self._append_to_log_file(message)

    def _append_to_log_file(self, log_message: Dict[str, Any]):
        """
        Append a log message to the current log file, using a temporary file to ensure atomicity.

        :param log_message: The log message as a dictionary.
        """
        temp_log_path = self.current_log_path.with_suffix('.tmp')

        if self.current_log_path.exists():
            with open(self.current_log_path, 'r') as log_file:
                try:
                    data = json.load(log_file)
                    if not isinstance(data, list):
                        data = [data]
                except json.JSONDecodeError:
                    data = []
                data.append(log_message)
        else:
            data = [log_message]

        with open(temp_log_path, 'w') as temp_log_file:
            json.dump(data, temp_log_file, indent=4)

        if self.current_log_path.exists():
            self.current_log_path.unlink()  # Remove the existing log file

        temp_log_path.rename(self.current_log_path)  # Rename the temp file to the log file


    def _merge_dicts(self, dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
        """
        Merge two dictionaries recursively.

        :param dict1: The first (base) dictionary.
        :param dict2: The second (delta update) dictionary.
        :return: The merged dictionary.
        """
        for key, value in dict2.items():
            if key in dict1:
                if isinstance(dict1[key], dict) and isinstance(value, dict):
                    self._merge_dicts(dict1[key], value)
                elif isinstance(dict1[key], list) and isinstance(value, list):
                    dict1[key].extend(value)
                elif type(dict1[key]) is not type(value):
                    raise ValueError(f"Conflict at key '{key}': {dict1[key]} vs {value}")
                else:
                    dict1[key] = value
            else:
                dict1[key] = value
        return dict1

    def merge_logs(self) -> Dict[str, Any]:
        """
        Merge all log files into a single dictionary.

        :return: The merged dictionary.
        """
        merged_data = {}
        log_files = sorted(self.log_dir.glob(f"log_{self.log_name}_*.json"))

        for log_file in log_files:
            with open(log_file, 'r') as file:
                try:
                    data = json.load(file)
                    for entry in data:
                        merged_data = self._merge_dicts(merged_data, entry)
                except json.JSONDecodeError:
                    self.logger.error(f"Error reading log file: {log_file}")

        return merged_data
    


# Example Usage
if __name__ == "__main__":
    from pydantic import BaseModel, ValidationError

    delta_logger = DictDeltaLogger("example_log", log_dir="logs", max_files=5)

    for i in range(10):
        message = {
            "key1": f"Value {i}",
            "key2": i,
            "key3": {f"nested_key_{i:3d}": f"Nested value {i}"}
        }

        # directly log the dict message
        # delta_logger.log(message)

        class LogMessageModel(BaseModel):
            key1: str
            key2: int
            key3: Dict[str, Any]

        # Validate the message using the Pydantic model
        try:
            validated_message = LogMessageModel(**message)
            # Log the validated message
            delta_logger.log(validated_message.model_dump())
        except ValidationError as e:
            print(f"Validation error: {e}")
    
    merged_logs = delta_logger.merge_logs()
    print(json.dumps(merged_logs, indent=4))
