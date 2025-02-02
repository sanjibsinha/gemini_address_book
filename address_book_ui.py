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
