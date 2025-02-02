# address_book.py (Main application file)

from address_book_data import load_contacts, save_contacts
from address_book_ui import display_menu, get_user_input, display_contacts, get_contact_details

def main():
    """Main function to run the address book application."""

    contacts = load_contacts()  # Load contacts from a file (more on this later)

    while True:
        display_menu()  # Display the menu options

        choice = get_user_input("Enter your choice: ")  # Get user input

        if choice == '1':  # Add contact
            new_contact = get_contact_details()  # Get contact details from user
            if new_contact: # Check if the user provided valid contact details
                contacts.append(new_contact)  # Add the new contact to the list
                print("Contact added successfully!")
            else:
                print("Invalid contact details. Please try again.")


        elif choice == '2':  # View contacts
            display_contacts(contacts)  # Display the contacts
        elif choice == '3':  # Search contact (Implementation for you to try!)
            search_term = get_user_input("Enter search term: ")
            #Implement your search logic here.
            pass # Placeholder - You'll implement search functionality
        elif choice == '4':  # Delete contact (Implementation for you to try!)
             #Implement your delete logic here.
             pass # Placeholder - You'll implement delete functionality
        elif choice == '5':  # Save and Exit
            save_contacts(contacts)  # Save contacts to file
            print("Contacts saved. Exiting.")
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Start the application
