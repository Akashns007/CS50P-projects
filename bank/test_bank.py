from bank import value

def main():
    test_zero()
    test_20()
    test_100()


def test_zero():
    assert value('hello gi')==0
    assert value('Hello')==0
    assert value('HeLlO Gi')==0

def test_20():

    assert value('hi')==20
    assert value('hey')==20


def test_100():
    assert value('good moring')==100
    assert value("what's up")==100




if __name__ == "__main__":
    main()