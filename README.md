# gemini_address_book

## Code written by Gemini

Alright, let's build a simple address book in Python, focusing on modularity and explaining the syntax as we go.  We'll structure it so you can easily expand it later.

```python
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



# address_book_data.py (Handles data storage)

import json  # For working with JSON data (we'll use JSON to store data)

def load_contacts(filename="contacts.json"):
    """Loads contacts from a JSON file."""
    try:
        with open(filename, 'r') as f:  # 'with' ensures the file is closed properly
            return json.load(f)  # Load JSON data from the file
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

def save_contacts(contacts, filename="contacts.json"):
    """Saves contacts to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(contacts, f, indent=4)  # Dump contacts to JSON file with indentation

# address_book_ui.py (Handles user interface)

def display_menu():
    """Displays the menu options."""
    print("\nAddress Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Save and Exit")

def get_user_input(prompt):
    """Gets user input with a prompt."""
    return input(prompt)

def get_contact_details():
    """Gets contact details from the user."""
    name = get_user_input("Enter name (or type 'cancel' to go back): ")
    if name.lower() == 'cancel':
        return None

    phone = get_user_input("Enter phone number: ")
    email = get_user_input("Enter email (optional): ")

    # We can add validation here later
    if not name or not phone:
        print("Name and Phone number are required.")
        return None
    
    return {"name": name, "phone": phone, "email": email}

def display_contacts(contacts):
    """Displays the contacts in a formatted way."""
    if not contacts:
        print("No contacts found.")
        return
    
    print("-" * 30)  # Separator
    for i, contact in enumerate(contacts):
        print(f"{i+1}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        if contact.get('email'): # Check if email exists before printing
            print(f"   Email: {contact['email']}")
        print("-" * 30)


```

**Explanation and Key Concepts:**

1.  **Modularity:** The code is split into three files:
    *   `address_book.py`: The main application logic.
    *   `address_book_data.py`: Handles loading and saving contact data.
    *   `address_book_ui.py`: Manages the user interface (displaying menus, getting input, etc.).  This separation makes the code more organized and easier to maintain.

2.  **`if __name__ == "__main__":`**: This crucial line ensures that the `main()` function is only called when you run `address_book.py` directly (not when you import it as a module into another script).

3.  **Data Storage (JSON):** We use the `json` module to store the contacts in a file named `contacts.json`.  JSON (JavaScript Object Notation) is a simple, human-readable format for storing data.  `json.load()` reads JSON data from a file, and `json.dump()` writes data to a JSON file.

4.  **Functions:**  The code makes heavy use of functions, which are reusable blocks of code. This makes the program more organized and easier to read.

5.  **Lists and Dictionaries:** Contacts are stored in a list of dictionaries.  Each dictionary represents a single contact and contains the contact's name, phone, and email.

6.  **Error Handling (try-except):** The `load_contacts()` function uses a `try-except` block to handle the case where the `contacts.json` file doesn't exist. This prevents the program from crashing.

7.  **User Input:** The `input()` function is used to get input from the user.

8.  **String Formatting (f-strings):**  We use f-strings (e.g., `f"Name: {contact['name']}"`) to make it easier to create formatted strings.

9. **Data Validation:** In `get_contact_details()`, we've added a basic check to ensure that the user provides a name and phone number. You can enhance this validation to check for valid phone numbers or email formats.

**Next Steps (Your Tasks):**

*   **Search Functionality:** Implement the search functionality in `address_book.py`.  You'll need to get a search term from the user and then loop through the `contacts` list to find matching contacts.
*   **Delete Functionality:** Implement the delete functionality.  You'll need to let the user choose a contact to delete and then remove it from the list.
*   **More Robust Validation:** Add more validation to the `get_contact_details()` function to check for valid phone numbers, email addresses, etc.
*   **User Interface Enhancements:** You can improve the user interface by using libraries like `rich` or `curses` to create a more visually appealing menu.
