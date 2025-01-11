library = {}

def display_menu():
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. View Books")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Exit")

def add_book():
    book = input("Enter the book name: ")
    library[book] = 'available'
    print(f"Book '{book}' added successfully!")

def view_books():
    if not library:
        print("No books in the library!")
        return
    print("\nLibrary Books:")
    for book, status in library.items():
        print(f"{book} - {'Available' if status == 'available' else 'Borrowed'}")

def borrow_book():
    view_books()
    if not library:
        return
    book = input("\nEnter the name of the book to borrow: ")
    if library.get(book) == 'available':
        library[book] = 'borrowed'
        print(f"You have borrowed '{book}'.")
    else:
        print("Book not available or doesn't exist!")

def return_book():
    book = input("Enter the name of the book to return: ")
    if library.get(book) == 'borrowed':
        library[book] = 'available'
        print(f"Book '{book}' returned successfully!")
    else:
        print("This book is not borrowed or doesn't exist!")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                add_book()
            elif choice == 2:
                view_books()
            elif choice == 3:
                borrow_book()
            elif choice == 4:
                return_book()
            elif choice == 5:
                print("Exiting Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
