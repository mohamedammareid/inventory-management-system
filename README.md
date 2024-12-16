# 🛒 Inventory Management System

## Overview

The **Inventory Management System** is a Python-based program that allows users to manage their inventory with functionalities to add, remove, view, update, and search items. It also provides basic statistics about the inventory, such as total value and most expensive items.

## Features

1. **Add Item ➕**
   - Add new items to the inventory by specifying their name, quantity, and price.
  
2. **Remove Item ➖**
   - View the current inventory and choose an item to remove.

3. **View Inventory 📋**
   - Display all the items in the inventory with their quantities, prices, and dates added.

4. **Update Item 🔄**
   - Update the details (quantity and price) of an existing item in the inventory.

5. **View Statistics 📊**
   - View statistics about the inventory, including the total value of the inventory, the most expensive item, and the total number of items.

6. **Search Item 🔍**
   - Search for items in the inventory by their name or part of their name.

7. **Exit 🚪**
   - Exit the program.

## Installation

1. **Download the repository** or clone it using Git:
   ```bash
   git clone https://github.com/your-username/inventory-management-system.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd inventory-management-system
   ```

3. **Ensure you have Python installed** (Python 3.x recommended). You can verify this by running:
   ```bash
   python --version
   ```

4. **Install required dependencies** (if any, for this program it's just standard Python libraries).

## Running the Program

1. **To run the program, simply execute the Python script**:

   ```bash
   python import_json.py
   ```

2. **Follow the on-screen prompts** to navigate through the menu options.

## File Structure

- **import_json.py**: The main script for running the Inventory Management System.
- **inventory.json**: The file where inventory data is saved and loaded from.

## Example Usage

When you run the program, you will see the following main menu:

```
🛒 Inventory Management System

1. Add item ➕
2. Remove item ➖
3. View inventory 📋
4. Update item 🔄
5. View statistics 📊
6. Search item 🔍
7. Exit 🚪
```

### Adding an Item

1. Choose option 1 (`Add item`).
2. Enter the item name, quantity, and price.
3. The item will be added to the inventory.

### Removing an Item

1. Choose option 2 (`Remove item`).
2. Select an item to remove by number.
3. The item will be removed from the inventory.

### Viewing the Inventory

1. Choose option 3 (`View inventory`).
2. The current inventory will be displayed with item details like quantity, price, and date added.

### Updating an Item

1. Choose option 4 (`Update item`).
2. Select an item to update by number.
3. Enter the new quantity and price to update the item.

### Viewing Statistics

1. Choose option 5 (`View statistics`).
2. View total value, most expensive item, and total number of items in the inventory.

### Searching for an Item

1. Choose option 6 (`Search item`).
2. Enter the name or part of the name to search for items.

### Exiting the Program

1. Choose option 7 (`Exit`).
2. The program will exit.



