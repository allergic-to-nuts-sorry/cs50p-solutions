from datetime import date
from seasons import mins, parse_date


def test_parse_date():
    # Valid dates should return date objects
    assert parse_date("2000-01-01") == date(2000, 1, 1)

    # Invalid formats should return None
    assert parse_date("January 1, 2000") is None
    assert parse_date("2000-13-01") is None


def test_mins():
    # Test with a mock date relative to today or exact timedelta days
    # 365 days = 525,600 minutes
    one_year_ago = date.today() - date(2025, 1, 1)  # Or test a fixed timedelta
    # Example assertion using a fixed date diff:
    past_date = date.today().replace(year=date.today().year - 1)
    assert mins(past_date) == "Five hundred twenty-five thousand, six hundred minutes"
