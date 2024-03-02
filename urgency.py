import random

class Contact:
    def __init__(self, name, phone_number, priority):
        self.name = name
        self.phone_number = phone_number
        self.priority = priority

def load_contacts():
    # Randomly generate contacts
    contacts_data = [
        ("Shayenne", "+145678005", "urgent"),
        ("Clampsun", "+44338762", "high"),
        ("Reddihe", "+219645902", "low"),
        ("Beatek", "+256346998", "low"),
        ("Liamsworth", "+335678025", "high"),
        ("Sly", "+423541544", "urgent")
    ]

    # Create Contact objects
    contacts = [Contact(name, phone_number, priority) for name, phone_number, priority in contacts_data]

    return contacts

def adjust_contacts_priority(contacts):
    contacts.sort(key=lambda x: x.priority, reverse=True)
    return contacts

def evaluate_call(caller, contacts):
    for contact in contacts:
        if caller == contact.name:
            if contact.priority == 'urgent':
                print(f"Answering urgent call from {caller}")
                return
            elif contact.priority == 'high':
                print(f"Sending high priority call from {caller} to voicemail")
                return
            else:
                print(f"Hanging up on low priority call from {caller}")
                return
    print(f"Hanging up on unknown caller {caller}")

def main():
    # Load contacts and adjust priority
    contacts = load_contacts()
    contacts = adjust_contacts_priority(contacts)

    # Simulate incoming calls
    random_caller = random.choice(["John", "Jane", "Alice", "Bob", "Charlie", "David", "Unknown"])
    evaluate_call(random_caller, contacts)

if __name__ == "__main__":
    main()
