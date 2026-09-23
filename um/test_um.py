from um import count
import pytest

def test_words_containing_um():
    assert count("yummy") == 0
    assert count("umwah") == 0

def test_sentences_with_um():
    assert count("um, i dont know what to say") == 1
    assert count("that will be um 30 euros") == 1
    assert count("um, wait a min, um, i was saying, um") == 3

def test_regular():
    assert count("hello i have a puppy") == 0
    assert count("it is a labrador") == 0

def test_case_insensitivity():
    # Test upper, lower, and mixed case variations of "um"
    assert count("Um, thanks for the assistance.") == 1
    assert count("UM, hello, um") == 2
    assert count("uM, is this UM, working?") == 2
