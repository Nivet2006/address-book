# function to add contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    contact = f"{name},{phone},{email}\n"
    
    with open("address_book.txt", "a") as file:
        file.write(contact)
    
    print("Contact added successfully!")

# function to view contact
def view_contacts():
    with open("address_book.txt", "r") as file:
        contacts = file.readlines()
    
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            name, phone, email = contact.strip().split(",")
            print(f"Name: {name}\tPhone: {phone}\tEmail: {email}")

# function to search contact
def search_contact():
    term = input("Enter search term: ")
    
    with open("address_book.txt", "r") as file:
        contacts = file.readlines()
    
    matching_contacts = []
    for contact in contacts:
        if term.lower() in contact.lower():
            matching_contacts.append(contact)
    
    if not matching_contacts:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for contact in matching_contacts:
            name, phone, email = contact.strip().split(",")
            print(f"Name: {name}\tPhone: {phone}\tEmail: {email}")

# function to delete contact
def delete_contact():
    term = input("Enter search term: ")
    
    with open("address_book.txt", "r") as file:
        contacts = file.readlines()
    
    matching_contacts = []
    for contact in contacts:
        if term.lower() in contact.lower():
            matching_contacts.append(contact)
    
    if not matching_contacts:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for i, contact in enumerate(matching_contacts, start=1):
            name, phone, email = contact.strip().split(",")
            print(f"{i}. Name: {name}\tPhone: {phone}\tEmail: {email}")
        
        choice = input("Enter the number of the contact to delete: ")
        try:
            index = int(choice) - 1
            contact_to_delete = matching_contacts[index]
            contacts.remove(contact_to_delete)
            
            with open("address_book.txt", "w") as file:
                file.writelines(contacts)
            
            print("Contact deleted successfully!")
        except (ValueError, IndexError):
            print("Invalid choice.")

# Main program 
# added looping
while True:
    print("\n***** Address Book *****")
    print("1. -> Add Contact")
    print("2. -> View Contacts")
    print("3. -> Search Contact")
    print("4. -> Delete Contact")
    print("5. -> Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Thank you for using the Address Book!")
        break
    else:
        print("Invalid choice. Please try again.")
