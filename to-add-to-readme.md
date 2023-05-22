5. Use the menu options to interact with the Address Book program:

---Add Contact: Allows you to add a new contact by providing the name, phone number, and email address.
---View Contacts: Displays all the stored contacts in a formatted manner.
---Search Contact: Enables you to search for contacts by providing a search term (e.g., name) and displays the matching contacts.
---Delete Contact: Allows you to delete contacts by providing a search term (e.g., name) and selecting the contact to delete from the matching contacts.
6. To exit the program, select the "Quit" option from the menu.

# Data Storage
The contact information is stored in a text file called "address_book.txt". Each line in the file represents a contact and contains the contact details separated by commas. The format for each contact is as follows:

```Name,Phone,Email```

For example:


```John Smith,1234567890,john@example.com```

# Notes
---The Address Book program utilizes file handling to read from and write to the "address_book.txt" file. Ensure that the program has appropriate read and write permissions to access the file.

---The program assumes that the "address_book.txt" file is located in the same directory as the address_book.py file. If you want to store the file in a different location, modify the file path in the code accordingly.

---This implementation provides a basic framework for an Address Book using file handling. You can extend the program and add more features to enhance its functionality as per your requirements.

# Conclusion
The Address Book program offers a simple and user-friendly way to manage contacts through a command-line interface. It provides essential functionalities to add, view, search, and delete contacts. By using file handling, contact information is stored in a text file, making it easy to access and manage. Feel free to customize and enhance the program according to your needs and preferences.