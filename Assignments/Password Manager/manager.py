import os

passwords = {}

def display_menu():
    print("\nPassword Manager")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

def add_password():
    site = input("Enter the website or service: ")
    password = input("Enter the password: ")
    passwords[site] = password
    print(f"Password for '{site}' added successfully!")

def view_passwords():
    if not passwords:
        print("No passwords saved!")
        return
    print("\nSaved Passwords:")
    for site, password in passwords.items():
        print(f"{site}: {password}")

def save_passwords_to_file():
    with open("passwords.txt", "w") as file:
        for site, password in passwords.items():
            file.write(f"{site}|{password}\n")

def load_passwords_from_file():
    global passwords
    if not os.path.exists("passwords.txt"):
        return
    with open("passwords.txt", "r") as file:
        for line in file:
            site, password = line.strip().split("|")
            passwords[site] = password

def main():
    load_passwords_from_file()
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                add_password()
            elif choice == 2:
                view_passwords()
            elif choice == 3:
                save_passwords_to_file()
                print("Passwords saved. Exiting Password Manager. Goodbye!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
