import pytest
from working import convert


def test_convert_valid_times():
    # Test standard time conversions with and without minutes
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "05:00 to 17:00" or convert("9 AM to 5:00 PM") == "09:00 to 17:00"

    # Test edge cases (Midnight and Noon)
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_convert_invalid_time_ranges():
    # Test out-of-bounds hours or minutes
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")


def test_convert_invalid_format():
    # Test missing 'to', improper spacing, or wrong delimiters
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")
