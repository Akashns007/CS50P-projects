from twttr import shorten

def main():
    test_case()
    test_numbers()
    test_punctuation()


def test_case():
    assert shorten("hello")=="hll"
    assert shorten("TWITTER")=="TWTTR"
    assert shorten("TwItTeR")=="TwtTR"

def test_numbers():
    assert shorten("1234")=="1234"


def test_punctuation():
    assert shorten("!?,.")=="!?,."



if __name__=="__main__":
    main()