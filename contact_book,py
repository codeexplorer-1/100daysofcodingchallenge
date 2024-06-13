class Contact:
  def __init__(self, name, phone_number, email):
    self.name = name
    self.phone_number = phone_number
    self.email = email

  def __str__(self):
    return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\n"

class ContactBook:
  def __init__(self):
    self.contacts = []

  def add_contact(self, contact):
    self.contacts.append(contact)

  def edit_contact(self, name, new_contact):
    for i, contact in enumerate(self.contacts):
      if contact.name == name:
        self.contacts[i] = new_contact
        return

    print(f"Contact '{name}' not found.")

  def delete_contact(self, name):
    for i, contact in enumerate(self.contacts):
      if contact.name == name:
        del self.contacts[i]
        return

    print(f"Contact '{name}' not found.")

  def search_contact(self, name):
    for contact in self.contacts:
      if contact.name == name:
        return contact

    return None

  def list_all_contacts(self):
    for contact in self.contacts:
      print(contact)

def main():
  contact_book = ContactBook()

  while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. List All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
      name = input("Enter contact name: ")
      phone_number = input("Enter phone number: ")
      email = input("Enter email (optional): ")
      contact = Contact(name, phone_number, email)
      contact_book.add_contact(contact)
      print("Contact added successfully!")

    elif choice == '2':
      name = input("Enter name of contact to edit: ")
      new_name = input("Enter new name (optional): ")
      new_phone_number = input("Enter new phone number (optional): ")
      new_email = input("Enter new email (optional): ")
      new_contact = Contact(new_name or name, new_phone_number or None, new_email or None)
      contact_book.edit_contact(name, new_contact)

    elif choice == '3':
      name = input("Enter name of contact to delete: ")
      contact_book.delete_contact(name)

    elif choice == '4':
      name = input("Enter name of contact to search: ")
      contact = contact_book.search_contact(name)
      if contact:
        print(contact)
      else:
        print("Contact not found.")

    elif choice == '5':
      contact_book.list_all_contacts()

    elif choice == '6':
      break

    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
