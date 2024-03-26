from plates import is_valid

def main():
    test_len()
    test_True()
    test_False()


def test_len():
    assert is_valid("wade")==1
    assert is_valid("w")==0
    assert is_valid("wadesahita")==0
    assert is_valid("Wdeit8")==1
    assert is_valid("98")==0

def test_True():
    assert is_valid("wade98")==1
    assert is_valid("wa89")==1
    assert is_valid("cs50")==1
    assert is_valid("AaA222")==1

def test_False():
    assert is_valid("78wade")==0
    assert is_valid("wa67de")==0
    assert is_valid("w a78d e")==0
    assert is_valid("Wade09")==0
    assert is_valid("cs05")==0
    assert is_valid("Aa22a")==0
    assert is_valid("wa 89")==0
    assert is_valid("wa?89")==0
    assert is_valid("wa!89")==0
    assert is_valid("wa.67")==0





if __name__== "__main__":
    main()