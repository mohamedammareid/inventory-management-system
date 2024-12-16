import os
import json
from datetime import datetime

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main menu function
def main_menu():
    clear_screen()
    print("🛒 Inventory Management System")
    print("\n1. Add item ➕")
    print("2. Remove item ➖")
    print("3. View inventory 📋")
    print("4. Update item 🔄")
    print("5. View statistics 📊")
    print("6. Search item 🔍")
    print("7. Exit 🚪")
    action = input("\nType the action: ").strip().lower()

    if action == 'add item' or action == '1':
        add_item()
    elif action == 'remove item' or action == '2':
        remove_item()
    elif action == 'view inventory' or action == '3':
        view_inventory()
    elif action == 'update item' or action == '4':
        update_item()
    elif action == 'view statistics' or action == '5':
        view_statistics()
    elif action == 'search item' or action == '6':
        search_item()
    elif action == 'exit' or action == '7':
        exit_program()
    else:
        print("\nInvalid choice. Please try again.")
        input("\nPress Enter to return to the main menu.")
        main_menu()

# Add item function
def add_item():
    clear_screen()
    print("📦 Add Item")
    item_name = input("\nEnter item name: ").strip()
    item_quantity = int(input("🔢 Enter item quantity: "))
    item_price = float(input("💲 Enter item price: "))
    item_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    inventory[item_name] = {
        'quantity': item_quantity,
        'price': item_price,
        'date_added': item_date,
    }

    save_inventory()
    print("\nItem added successfully!")
    input("\nPress Enter to return to the main menu.")
    main_menu()

# Remove item function
def remove_item():
    clear_screen()
    print("➖ Remove Item")

    if not inventory:
        print("\nNo items in the inventory to remove.")
        input("\nPress Enter to return to the main menu.")
        main_menu()
        return

    print("Current Inventory:")
    for index, item_name in enumerate(inventory, 1):
        print(f"{index}. {item_name} - Quantity: {inventory[item_name]['quantity']} - Price: ${inventory[item_name]['price']}")

    try:
        choice = int(input("\nEnter the number of the item you want to remove: "))
        if 1 <= choice <= len(inventory):
            item_name_to_remove = list(inventory.keys())[choice - 1]
            del inventory[item_name_to_remove]
            save_inventory()
            print(f"\n{item_name_to_remove} has been removed from the inventory.")
        else:
            print("\nInvalid choice. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

    input("\nPress Enter to return to the main menu.")
    main_menu()

# View inventory function
def view_inventory():
    clear_screen()
    print("📋 Current Inventory:\n")
    if not inventory:
        print("No items in the inventory.")
    else:
        for item_name, item_info in inventory.items():
            print(f"📦 {item_name} - Quantity: {item_info['quantity']} - Price: ${item_info['price']} - Added on: {item_info['date_added']}")
    input("\nPress Enter to return to the main menu.")
    main_menu()

# Update item function
def update_item():
    clear_screen()
    print("🔄 Update Item")

    if not inventory:
        print("\nNo items in the inventory to update.")
        input("\nPress Enter to return to the main menu.")
        main_menu()
        return

    print("Current Inventory:")
    for index, item_name in enumerate(inventory, 1):
        print(f"{index}. {item_name} - Quantity: {inventory[item_name]['quantity']} - Price: ${inventory[item_name]['price']} - Added on: {inventory[item_name]['date_added']}")

    try:
        choice = int(input("\nEnter the number of the item you want to update: "))
        if 1 <= choice <= len(inventory):
            item_name_to_update = list(inventory.keys())[choice - 1]
            new_quantity = int(input(f"Enter new quantity for {item_name_to_update}: "))
            new_price = float(input(f"Enter new price for {item_name_to_update}: "))

            inventory[item_name_to_update]['quantity'] = new_quantity
            inventory[item_name_to_update]['price'] = new_price
            save_inventory()
            print(f"\n{item_name_to_update} has been updated successfully!")
        else:
            print("\nInvalid choice. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

    input("\nPress Enter to return to the main menu.")
    main_menu()

# Search item function
def search_item():
    clear_screen()
    print("🔍 Search Item")
    search_query = input("\nEnter item name or part of it to search: ").strip().lower()

    found_items = [item_name for item_name in inventory if search_query in item_name.lower()]

    if not found_items:
        print(f"\nNo items found for '{search_query}'.")
    else:
        print(f"\nItems matching '{search_query}':")
        for item_name in found_items:
            item_info = inventory[item_name]
            print(f"📦 {item_name} - Quantity: {item_info['quantity']} - Price: ${item_info['price']} - Added on: {item_info['date_added']}")

    input("\nPress Enter to return to the main menu.")
    main_menu()

# View statistics function
def view_statistics():
    clear_screen()
    print("📊 Statistics:\n")

    if not inventory:
        print("No items in the inventory to show statistics.")
    else:
        total_value = sum(item['quantity'] * item['price'] for item in inventory.values())
        print(f"Total value of inventory: ${total_value:.2f}")
        most_expensive_item = max(inventory.items(), key=lambda x: x[1]['price'])
        print(f"Most expensive item: {most_expensive_item[0]} - ${most_expensive_item[1]['price']}")
        total_items = len(inventory)
        print(f"Total number of items: {total_items}")

    input("\nPress Enter to return to the main menu.")
    main_menu()

# Exit program function
def exit_program():
    clear_screen()
    print("🚪 Exiting the program. Goodbye!")
    exit()

# Load inventory from file
def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save inventory to file
def save_inventory():
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file)

# Main program execution
inventory = load_inventory()

if __name__ == "__main__":
    main_menu()
