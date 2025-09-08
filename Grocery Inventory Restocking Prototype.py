# This is where we'll store our grocery items
# It's a dictionary that will look like: 
# {"Milk": {"stock": 10, "low_limit": 5}}
grocery_inventory = {}

def show_menu():
    """Shows the main menu to the user"""
    print("\n" + "="*40)
    print("       GROCERY INVENTORY MANAGER")
    print("="*40)
    print("1. View all items")
    print("2. Check what needs restocking")
    print("3. Add new item")
    print("4. Update item stock")
    print("5. Exit")
    print("="*40)

def view_all_items():
    """Shows all items in the inventory"""
    if not grocery_inventory:
        print("\nYour inventory is empty! Add some items first.")
        return
    
    print("\n--- CURRENT INVENTORY ---")
    for item_name, item_info in grocery_inventory.items():
        stock = item_info['stock']
        low_limit = item_info['low_limit']
        status = "OK" if stock > low_limit else "LOW STOCK!"
        print(f"{item_name}: {stock} units (alert at {low_limit}) - {status}")

def check_restock():
    """Checks which items need to be restocked"""
    if not grocery_inventory:
        print("\nNo items to check! Add some items first.")
        return
    
    print("\n--- RESTOCKING ALERTS ---")
    needs_restock = False
    
    for item_name, item_info in grocery_inventory.items():
        if item_info['stock'] <= item_info['low_limit']:
            needs_restock = True
            print(f"⚠️  RESTOCK {item_name}: Only {item_info['stock']} left! (Alert at {item_info['low_limit']})")
    
    if not needs_restock:
        print("All items have enough stock! ✅")

def add_new_item():
    """Adds a new item to the inventory"""
    print("\n--- ADD NEW ITEM ---")
    
    # Get item name
    item_name = input("Enter item name: ").title()
    
    # Check if item already exists
    if item_name in grocery_inventory:
        print(f"{item_name} is already in your inventory!")
        return
    
    # Get stock information
    try:
        current_stock = int(input("Current stock quantity: "))
        low_limit = int(input("Low stock alert level: "))
        
        # Basic validation
        if current_stock < 0 or low_limit < 0:
            print("Please enter positive numbers!")
            return
            
        # Add to inventory
        grocery_inventory[item_name] = {
            'stock': current_stock,
            'low_limit': low_limit
        }
        
        print(f"✅ {item_name} added successfully!")
        
    except ValueError:
        print("Please enter numbers only!")

def update_stock():
    """Updates the stock level of an item"""
    if not grocery_inventory:
        print("\nNo items to update! Add some items first.")
        return
    
    print("\n--- UPDATE STOCK ---")
    view_all_items()
    
    # Get item name
    item_name = input("\nEnter item name to update: ").title()
    
    if item_name not in grocery_inventory:
        print(f"{item_name} not found in inventory!")
        return
    
    # Get stock change
    try:
        change = int(input("Enter change (+ for add, - for sell): "))
        new_stock = grocery_inventory[item_name]['stock'] + change
        
        if new_stock < 0:
            print("Can't have negative stock!")
        else:
            grocery_inventory[item_name]['stock'] = new_stock
            print(f"✅ {item_name} updated! New stock: {new_stock}")
            
    except ValueError:
        print("Please enter a number!")

# Main program starts here
print("Welcome to Simple Grocery Manager!")
print("I'll help you track your store inventory.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == '1':
        view_all_items()
    elif choice == '2':
        check_restock()
    elif choice == '3':
        add_new_item()
    elif choice == '4':
        update_stock()
    elif choice == '5':
        print("\nThank you for using Grocery Manager! Goodbye! 👋")
        break
    else:
        print("Please enter a number between 1-5!")

    # Pause so user can read the output
    input("\nPress Enter to continue...")