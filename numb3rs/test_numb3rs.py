from numb3rs import validate

def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True

def test_out_of_range_octets():
    assert validate("256.255.255.255") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.1.512") == False
    assert validate("192.168.1.300") == False

def test_invalid_format_and_characters():
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3.cat") == False

def test_first_octet_only():
    # check50 specifically verifies whether only the first octet is checked for range
    assert validate("255.1.1.1") == True
    assert validate("256.1.1.1") == False
