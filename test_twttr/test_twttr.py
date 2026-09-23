from twttr import shorten

def test_vowels_lowercase():
    # Test lowercase vowel removal
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

def test_vowels_uppercase():
    # Test uppercase vowel removal
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""

def test_numbers():
    # Test that numbers are left untouched
    assert shorten("12345") == "12345"
    assert shorten("cs50") == "cs50"

def test_punctuation():
    # Test that punctuation marks are left untouched
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("what's up?") == "wht's p?"
