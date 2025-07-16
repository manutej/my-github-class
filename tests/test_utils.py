"""
Tests for utility functions.
"""

import json
import os
import sys
import tempfile
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.utils import (
    chunks,
    filter_list,
    format_currency,
    get_file_size,
    read_json_file,
    validate_email,
    write_json_file,
)


class TestJsonFunctions:
    """Test suite for JSON utility functions."""
    
    def test_read_json_file(self):
        """Test reading JSON file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            test_data = {"name": "test", "value": 42}
            json.dump(test_data, f)
            temp_file = f.name
        
        try:
            result = read_json_file(temp_file)
            assert result == test_data
        finally:
            os.unlink(temp_file)
    
    def test_read_json_file_not_found(self):
        """Test reading non-existent JSON file."""
        with pytest.raises(FileNotFoundError):
            read_json_file("nonexistent.json")
    
    def test_write_json_file(self):
        """Test writing JSON file."""
        test_data = {"name": "test", "items": [1, 2, 3]}
        
        with tempfile.NamedTemporaryFile(mode='r', suffix='.json', delete=False) as f:
            temp_file = f.name
        
        try:
            write_json_file(temp_file, test_data)
            with open(temp_file, 'r') as f:
                result = json.load(f)
            assert result == test_data
        finally:
            os.unlink(temp_file)


class TestEmailValidation:
    """Test suite for email validation."""
    
    def test_valid_emails(self):
        """Test valid email addresses."""
        valid_emails = [
            "test@example.com",
            "user.name@domain.org",
            "user+tag@example.co.uk",
            "123@example.com",
        ]
        
        for email in valid_emails:
            assert validate_email(email) is True
    
    def test_invalid_emails(self):
        """Test invalid email addresses."""
        invalid_emails = [
            "invalid.email",
            "@example.com",
            "test@",
            "test@.com",
            "test..test@example.com",
            "",
        ]
        
        for email in invalid_emails:
            assert validate_email(email) is False


class TestCurrencyFormatting:
    """Test suite for currency formatting."""
    
    def test_usd_formatting(self):
        """Test USD currency formatting."""
        assert format_currency(1234.56) == "$1,234.56"
        assert format_currency(0) == "$0.00"
        assert format_currency(1000000) == "$1,000,000.00"
    
    def test_eur_formatting(self):
        """Test EUR currency formatting."""
        assert format_currency(1234.56, "EUR") == "€1,234.56"
        assert format_currency(0, "EUR") == "€0.00"
    
    def test_custom_currency(self):
        """Test custom currency formatting."""
        assert format_currency(1234.56, "GBP") == "1,234.56 GBP"


class TestUtilityFunctions:
    """Test suite for other utility functions."""
    
    def test_get_file_size(self):
        """Test getting file size."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("test content")
            temp_file = f.name
        
        try:
            size = get_file_size(temp_file)
            assert size == 12  # "test content" is 12 bytes
        finally:
            os.unlink(temp_file)
    
    def test_get_file_size_nonexistent(self):
        """Test getting size of non-existent file."""
        assert get_file_size("nonexistent.txt") is None
    
    def test_filter_list(self):
        """Test list filtering."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        evens = filter_list(numbers, lambda x: x % 2 == 0)
        assert evens == [2, 4, 6, 8, 10]
    
    def test_chunks(self):
        """Test list chunking."""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = chunks(data, 3)
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert result == expected
        
        result = chunks(data, 4)
        expected = [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
        assert result == expected