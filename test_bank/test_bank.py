from bank import value

def test_hello_exact():
    assert value("hello") == 0
    assert value("hello Newman") == 0

def test_hello_case_insensitive():
    assert value("HELLO") == 0
    assert value("Hello there") == 0

def test_h_starts():
    assert value("hey") == 20
    assert value("How you doing?") == 20
    assert value("HI") == 20

def test_other_greetings():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("123") == 100
