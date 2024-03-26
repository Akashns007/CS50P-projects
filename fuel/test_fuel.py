from fuel import convert,gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_zero_division()
    test_value()

def test_convert():
    assert convert("1/4")==25
    assert convert("2/4")==50
    assert convert("3/4")==75
    assert convert("1/100")==1
    assert convert("99/100")==99


def test_gauge():
    assert gauge(25)=="25%"
    assert gauge(50)=="50%"
    assert gauge(1)=="E"
    assert gauge(99)=="F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")

if __name__ == "__main__":
    main()