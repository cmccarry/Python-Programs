'''
CS 2520- Fall Semester 2023
Final Project- Online Shopping Cart
'''

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)
        print(f"\n~~~{item.item_name} added to cart~~~")

    def remove_item(self, removed_item):
        for item in self.cart_items:
            if item.item_name == removed_item:
                self.cart_items.remove(item)
                print(f"\n~~~{item.item_name} removed~~~")
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                item.item_quantity = modified_item.item_quantity
                print(f"\n~~~{item.item_name} modified~~~")
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum((item.item_quantity * item.item_price) for item in self.cart_items)

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()} \n")
        for item in self.cart_items:
            item.print_item_cost()
        print("\nTotal: $" + str(self.get_cost_of_cart()))

    def print_descriptions(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date} \n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

def print_menu():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

def execute_menu(choice, shopping_cart):
    # Add item to cart
    if choice == 'a':
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_description = input("Enter the item description:\n")
        item.item_price = float(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))
        shopping_cart.add_item(item)

    # Remove item from cart
    elif choice == 'r':
        item_name = input("Enter name of item to remove:\n")
        shopping_cart.remove_item(item_name)

    # Change item quantity
    elif choice == 'c':
        modified_item = ItemToPurchase()
        modified_item.item_name = input("Enter the item name:\n")
        modified_item.item_quantity = int(input("Enter the new quantity:\n"))
        shopping_cart.modify_item(modified_item)

    # Output items' descriptions
    elif choice == 'i':
        shopping_cart.print_descriptions()

    # Output shopping cart
    elif choice == 'o':
        shopping_cart.print_total()

    # Quit
    elif choice == 'q':
        print("\nThank you for shopping. Have a good day!\n")

def main():
    name = input("Enter customer's name: \n")
    date = input("Enter today's date: \n")

    print(f"\nCustomer name: {name} \
          \nToday's date: {date}")

    shopping_cart = ShoppingCart(name, date)

    while True:
        user_choice = ''
        print_menu()
        user_choice = (input("\nChoose an option: \n")).lower()
        while user_choice not in "arcioq" or len(user_choice) != 1:
           print("Please choose a valid option.")
           print_menu()
           user_choice = (input("\nChoose an option: \n")).lower()
        execute_menu(user_choice, shopping_cart)
        if user_choice == 'q':
            break
        
if __name__ == "__main__":
    main()
