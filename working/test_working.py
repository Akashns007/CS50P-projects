from working import convert
import pytest

def main():
    test_withmins()
    test_withoutmins()
    test_valerr()

def test_withmins():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 11:30 AM") == "10:30 to 11:30"
    assert convert("12:30 AM to 8:50 AM") == "00:30 to 08:50"

def test_withoutmins():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 5:00 PM") == "00:00 to 17:00"


def test_valerr():
    with pytest.raises(ValueError):
        convert("8:70 AM to 12:70 PM")
    with pytest.raises(ValueError):
        convert("9AM to 8PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 8 PM")


if __name__ == "__main__":
    main()
