from project import add_contact, search_contact, display_contacts

def main():
    test_1()
    test_2()
    test_3()

def test_1():
    assert add_contact("akash,123-345-5677,mrpeculiar@gmail.com,india") == ("akash","123-345-5677","mrpeculiar@gmail.com","india")

def test_2():
    assert search_contact("a") == True

def test_3():
    assert display_contacts("contacts.csv") == True
