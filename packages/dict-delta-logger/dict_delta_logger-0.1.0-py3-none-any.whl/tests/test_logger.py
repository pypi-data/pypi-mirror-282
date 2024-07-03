# tests/test_logger.py

import unittest
from dict_delta_logger import DictDeltaLogger
from pydantic import BaseModel, ValidationError
from typing import Dict, Any

class TestDeltaLogger(unittest.TestCase):
    def setUp(self):
        self.logger = DictDeltaLogger(log_name="test_log", log_dir="test_logs", max_files=2)

    def test_log_message(self):
        message = {
            "key1": "value1",
            "key2": 1,
            "key3": {"nested_key": "nested_value"}
        }

        class LogMessageModel(BaseModel):
            key1: str
            key2: int
            key3: Dict[str, Any]

        validated_message = LogMessageModel(**message)
        self.logger.log(validated_message.model_dump())

        merged_logs = self.logger.merge_logs()
        self.assertIn("key1", merged_logs)
        self.assertEqual(merged_logs["key1"], "value1")

if __name__ == "__main__":
    unittest.main()
