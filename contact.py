import csv
import os

filename = "contact.csv"


def load_contacts():
    contactlist = []
    if os.path.exists(filename):
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                
                nums = row["phone_num"].split("|")  
                contactlist.append({"name": row["name"], "phone_num": nums})
    return contactlist


def save_contacts(contactlist):
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["name", "phone_num"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for c in contactlist:
         
            writer.writerow({"name": c["name"], "phone_num": "|".join(c["phone_num"])})

contact = load_contacts()


def phone_number(pnumber):
    return len(pnumber) == 10 and pnumber.isdigit()


def add_contact(contactlist, name, number):
    if not phone_number(number):
        print("Invalid phone number")
        return

    for c in contactlist:
        if number in c["phone_num"]:
            print("Number already exists in contact list:", c['name'])
            return

    for c in contactlist:
        if c["name"].lower() == name.lower():
            c["phone_num"].append(number)
            print("Number added to existing contact", c['name'])
            save_contacts(contactlist)
            return

    contactlist.append({"name": name, "phone_num": [number]})
    save_contacts(contactlist)
    print("New contact added")


def search_contact(contactlist, name):
    for c in contactlist:
        if c["name"].lower() == name.lower():
            print(f"{c['name']} : {c['phone_num']}")
            return
    else:
        print("Contact not found")


def view_contact(contactlist):
    if len(contactlist) == 0:
        print("The contact list is empty")
    else:
        for c in contactlist:
            print(f"{c['name']} : {', '.join(c['phone_num'])}")


def update_contact(contactlist, name, new_number):
    if not phone_number(new_number):
        print("Invalid phone number")
        return

    for c in contactlist:
        if c["name"].lower() == name.lower():
            c["phone_num"] = [new_number]
            save_contacts(contactlist)
            print("Number updated successfully")
            return
    else:
        print("Contact not found")


def delete_contact(contactlist, name):
    for c in contactlist:
        if c["name"].lower() == name.lower():
            contactlist.remove(c)
            save_contacts(contactlist)
            print("Contact deleted successfully")
            return
    else:
        print("Contact not found")



while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))
        if choice < 1 or choice > 6:
            print("Invalid choice! Enter number between 1 and 6.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(contact, name, phone)

    elif choice == 2:
        view_contact(contact)

    elif choice == 3:
        name = input("Enter name to search: ")
        search_contact(contact, name)

    elif choice == 4:
        name = input("Enter name to update: ")
        new_number = input("Enter new phone number: ")
        update_contact(contact, name, new_number)

    elif choice == 5:
        name = input("Enter name to delete: ")
        delete_contact(contact, name)

    elif choice == 6:
        print("Exit")
        break