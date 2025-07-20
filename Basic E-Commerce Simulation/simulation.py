items = {
    "Laptop": 50000,
    "Headphones": 2000,
    "Smartphone": 30000,
    "Tablet": 15000,
    "Camera": 25000
}

cart = []

def display_items():
    print("\nAvailable Items:")
    for item, price in items.items():
        print(f"{item}: ₹{price}")

def add_to_cart():
    display_items()
    item = input("Enter the name of the item to add to the cart: ")
    if item in items:
        cart.append(item)
        print(f"{item} added to the cart!")
    else:
        print("Item not found!")

def view_cart():
    if not cart:
        print("Your cart is empty!")
        return
    print("\nYour Cart:")
    total = 0
    for item in cart:
        print(f"{item}: ₹{items[item]}")
        total += items[item]
    print(f"Total: ₹{total}")

def main():
    while True:
        print("\nE-Commerce Simulation")
        print("1. View Items")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_items()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
