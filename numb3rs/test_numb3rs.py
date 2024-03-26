from numb3rs import validate
import pytest

def main():
    test_numberstrue()
    test_numbersfalse()
    test_strings()



def test_numberstrue():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.0.0") == True
    assert validate("8.02.1.200") == True

def test_numbersfalse():
    assert validate("512.512.512.512")==False
    assert validate("1.2.3.1000")==False
    assert validate("1.555.555.555")==False


def test_strings():
    assert validate("cat")== False
    assert validate("dog")== False


if __name__ == "__main__":
    main()

