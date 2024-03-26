from seasons import birthday_check

def main():
    test_birthday_check()

def test_birthday_check():
    assert birthday_check("2003-08-25") == ("2003", "08", "25")
    assert birthday_check("2003-8-25") == None
    assert birthday_check("august 25, 2003") == None
  

if __name__ == "__main__":
    main()

