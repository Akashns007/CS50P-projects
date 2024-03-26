from um import count

def main():
    test_1()
    test_2()
    test_3()

def test_1():
    assert count("hello, um, world") == 1
    assert count("Um, thanks, um...") == 2

def test_2():
    assert count("um?") == 1
    assert count("//um,,,?") == 1
    assert count("um, hello...., um..,wafe") == 2

def test_3():
    assert count("assumption") == 0
    assert count("Um, thanks for the album.") == 1
    assert count("um, the chocolate pie is yummy") == 1
    assert count("Hello, world") == 0


if __name__ == "__main__":
    main()
