import re
import csv
from tabulate import tabulate

CONTACTS_FILE = "contacts.csv"


def main():
    while True:
        print("\n1. Add Contact\n2. Search Contact\n3. Display Contact\n4. Exit")
        n = input("Enter the option: ")

        if n == '1':
            add_contact(verify_details())
        elif n == '2':
            k_word = input("Enter the keyword to search: ")
            print(f"The search results for {k_word} are:\n")
            search_contact(k_word)
        elif n == '3':
            display_contacts(CONTACTS_FILE)
        elif n == '4':
            break
        else:
            print("Invalid option. Please enter a valid option.")


def verify_details():
    name = input("Enter the name: ")
    phone = input("Enter the Phone Number: ")
    if not re.match(r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$", phone):
        print("\nEntered phone number is in incorrect format!")
        return

    email = input("Enter the mail: ")
    if not re.match(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$", email):
        print("\nEmail in incorrect format!")
        return

    address = input("Enter the address: ")
    return f"{name},{phone},{email},{address}"

def add_contact(verify):

    name,phone,email,address = verify.split(",",3)
    with open(CONTACTS_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email, address])
        return name,phone,email,address

def search_contact(keyword):
    try:
        with open(CONTACTS_FILE, 'r', newline='') as file:
            reader = csv.DictReader(file)
            matching_rows = [row for row in reader if keyword.lower() in row['name'].lower() or keyword in row['phone']]

            if matching_rows:
                for row in matching_rows:
                    print(row)
                return True
            else:
                print(f"No matching results for '{keyword}' in file.")
    except FileNotFoundError:
        print(f"Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_contacts(c_file):
    try:
        with open(c_file, "r", newline='') as file:
            reader = csv.reader(file)
            headers = next(reader, None)  # Read the first row as headers
            if headers is not None:
                data = [row for row in reader]
                print(tabulate(data, headers=headers, tablefmt="pretty"))
                return True
            else:
                print("No contact data present.")
    except FileNotFoundError:
        print("No contact file present!")


if __name__ == "__main__":
    main()
