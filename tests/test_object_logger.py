import logging
import pytest
import io
import sys

from src.object_logger import log_object

class TestObjectLogger:
    def setup_method(self):
        # Capture log output
        self.log_capture = io.StringIO()
        self.log_handler = logging.StreamHandler(self.log_capture)
        logging.getLogger().addHandler(self.log_handler)
        logging.getLogger().setLevel(logging.DEBUG)

    def teardown_method(self):
        # Remove the log handler
        logging.getLogger().removeHandler(self.log_handler)

    def test_log_simple_dict(self):
        test_dict = {"name": "John", "age": 30}
        result = log_object(test_dict)
        log_output = self.log_capture.getvalue()
        
        assert '"name": "John"' in log_output
        assert '"age": 30' in log_output

    def test_log_nested_dict(self):
        test_dict = {"user": {"name": "Alice", "details": {"age": 25}}}
        result = log_object(test_dict)
        log_output = self.log_capture.getvalue()
        
        assert '"name": "Alice"' in log_output
        assert '"age": 25' in log_output

    def test_log_list(self):
        test_list = [1, 2, 3, {"a": 1}]
        result = log_object(test_list)
        log_output = self.log_capture.getvalue()
        
        assert "1" in log_output
        assert "2" in log_output
        assert '"a": 1' in log_output

    def test_log_custom_log_level(self):
        test_dict = {"test": "value"}
        result = log_object(test_dict, log_level=logging.DEBUG)
        log_output = self.log_capture.getvalue()
        
        assert '"test": "value"' in log_output

    def test_log_custom_logger(self):
        custom_logger = logging.getLogger('custom')
        custom_logger.setLevel(logging.INFO)
        custom_stream = io.StringIO()
        custom_handler = logging.StreamHandler(custom_stream)
        custom_logger.addHandler(custom_handler)

        test_dict = {"custom": "logger"}
        result = log_object(test_dict, logger=custom_logger)
        custom_log_output = custom_stream.getvalue()
        
        assert '"custom": "logger"' in custom_log_output

    def test_log_object_with_unprintable_object(self):
        class UnprintableObject:
            pass

        test_obj = UnprintableObject()
        result = log_object(test_obj)
        log_output = self.log_capture.getvalue()
        
        assert "UnprintableObject" in log_output

    def test_log_object_error_handling(self):
        # Test that an error is raised for truly unprintable objects
        class ComplexUnprintableObject:
            def __repr__(self):
                raise Exception("Cannot represent")

        with pytest.raises(TypeError):
            log_object(ComplexUnprintableObject())