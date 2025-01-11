expenses = []

def display_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

def add_expense():
    name = input("Enter the expense name: ")
    try:
        amount = float(input("Enter the amount: "))
        expenses.append({'name': name, 'amount': amount})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount!")

def view_expenses():
    if not expenses:
        print("No expenses recorded!")
        return
    print("\nYour Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['name']}: ${expense['amount']:.2f}")

def calculate_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                calculate_total()
            elif choice == 4:
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
