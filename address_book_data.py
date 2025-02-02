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
