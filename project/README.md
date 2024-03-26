# YOUR PROJECT TITLE
    #### Video Demo: https://youtu.be/94GjXJ72IIw?si=bZpRn8hqXQTYQF4I
    #### Description:

# Contact Manager =>
====================
A basic contact management system implemented in Python. Users can add contacts, search for contacts, and display all contacts.

## Features:-
-------------
- **Add Contact:** Allows the user to add a new contact with name, phone number, email, and address.
- **Search Contact:** Enables the user to search for contacts based on a keyword (name or phone number).
- **Display Contact:** Displays all contacts in a tabular format.
- **Exit:** Exits the program.

## Usage:-
----------
### Add Contact
----------------
1. Select option 1.
2. Enter the contact details when prompted.
3. Contacts are saved to the `contacts.csv` file.

### Search Contact
------------------
1. Select option 2.
2. Enter a keyword (name or phone number) to search for contacts.
3. Matching contacts will be displayed.

### Display Contact
-------------------
1. Select option 3.
2. All contacts will be displayed in a tabular format.

### Exit
--------
1. Select option 4 to exit the program.

## File Structure:-
-------------------
- "contacts.csv": CSV file to store contact details.
  - Note: Don't remove the first row in the file as it is the header.
          this is because if in case it is removed, then the csv dictreader
          may throw an error, so inorder for the csv reader to read the file
          the first line shouldn't be removed
- "main.py": Main program file containing the contact management logic.

## Requirements:-
-----------------
- Python 3.x
- `csv` module (included in Python standard library)
- `tabulate` module (`pip install tabulate`)
- `re` module (`pip install re`)

## How to Run:-
---------------
1. Clone the repository or download the `main.py` file.
2. Open a terminal and navigate to the directory containing `main.py`.
3. Run the program using the command:
   ```bash
   python main.py

## Debates:-
------------
1. Used csv instead of json because json file after every time the program is closed and ran again
    opened a new list to store the new details entered, it became a problem for the display_contacts
    function, to overcome that problem csv file type is used
2. the name of csv file can be changed but forget not to add the first row as name,phone,mail,address
3. regex is used to get the the details in correct pattern or order
4. tabulate is used to make the output look a bit more user friendly and easy to read


terminal:-
----------
- python main.py

Follow the on-screen instructions to use the Contact Manager.

Contributing:-
--------------
Feel free to contribute by opening issues or submitting pull requests.


thank you
---------
