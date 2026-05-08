import csv

#----------------------------------------- Staff Side --------------------------------------

# =========================================================
# Load menu from storage.csv
# =========================================================
def load_menu():

    try:
        with open("storage.csv", "r") as file:
            return list(csv.reader(file))

    except FileNotFoundError:
        print("ERROR: storage.csv not found.")
        return []


# =========================================================
# Save menu into storage.csv
# =========================================================
def save_menu(menu):

    with open("storage.csv", "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerows(menu)


# =========================================================
# Load orders from orders.csv
# =========================================================
def load_orders():

    try:
        with open("orders.csv", "r") as file:
            return list(csv.reader(file))

    except FileNotFoundError:
        print("ERROR: orders.csv not found.")
        return []


# =========================================================
# Save orders into orders.csv
# =========================================================
def save_orders(orders):

    with open("orders.csv", "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerows(orders)


# =========================================================
# Display all menu items
# =========================================================
def display_menu():

    menu = load_menu()

    print("\n========== MENU ==========")

    for i in range(len(menu)):

        item = menu[i]

        category = item[0]
        name = item[1]
        price = item[2]
        quantity = int(item[3])

        print(f"\n[{i + 1}] {name}")
        print("Category:", category)
        print("Price: RM", price)

        if quantity > 0:
            print("Quantity:", quantity)

        else:
            print("OUT OF STOCK")


# =========================================================
# Search menu item
# =========================================================
def search_item():

    menu = load_menu()

    search = input("\nEnter item name: ").lower()

    found = False

    for item in menu:

        category = item[0]
        name = item[1]
        price = item[2]
        quantity = int(item[3])

        # Search using full item name
        if search in name.lower():

            print("\n========== ITEM FOUND ==========")
            print("Name:", name)
            print("Category:", category)
            print("Price: RM", price)

            if quantity > 0:
                print("Quantity:", quantity)

            else:
                print("OUT OF STOCK")

            found = True

    if not found:
        print("Item not found.")


# =========================================================
# Add new menu item
# =========================================================
def add_item():
    menu = load_menu()
    print("\n===== ADD ITEM =====")
    category = input("Category: ")
    name = input("Item Name: ")
    price = input("Price: ")
    quantity = input("Quantity: ")
    print("\n===== CONFIRM ITEM =====")
    print("Category:", category)
    print("Name:", name)
    print("Price: RM", price)
    print("Quantity:", quantity)
    confirm = input("\nSave item? (Y/N): ")
    if confirm.upper() == "Y":

        menu.append([category, name, price, quantity])

        save_menu(menu)

        print("Item added successfully.")
    else:
        print("Cancelled.")


# =========================================================
# Update menu item
# =========================================================
def update_menu_item():

    menu = load_menu()

    display_menu()

    choice = input("\nSelect item number: ")

    if not choice.isdigit():
        print("Invalid input.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(menu):
        print("Invalid item number.")
        return

    item = menu[choice - 1]

    print("\nLeave blank to keep old value.")

    category = input("Category (" + item[0] + "): ")
    name = input("Name (" + item[1] + "): ")
    price = input("Price (" + item[2] + "): ")
    quantity = input("Quantity (" + item[3] + "): ")

    # Keep old values if blank
    if category == "":
        category = item[0]

    if name == "":
        name = item[1]

    if price == "":
        price = item[2]

    if quantity == "":
        quantity = item[3]

    print("\n===== CONFIRM UPDATE =====")
    print("Category:", category)
    print("Name:", name)
    print("Price: RM", price)
    print("Quantity:", quantity)

    confirm = input("\nSave changes? (Y/N): ")

    if confirm.upper() == "Y":

        menu[choice - 1] = [category, name, price, quantity]

        save_menu(menu)

        print("Item updated successfully.")

    else:
        print("Cancelled.")


# =========================================================
# Display grouped orders
# =========================================================
def display_orders():

    orders = load_orders()

    shown_orders = []

    print("\n========== ORDERS ==========")

    for order in orders:

        order_id = order[0]

        # Skip duplicate order IDs
        if order_id in shown_orders:
            continue

        shown_orders.append(order_id)

        print(f"\n[{len(shown_orders)}] Order ID: {order_id}")

        print("Customer:", order[3])
        print("Address:", order[4])
        print("Contact:", order[5])
        print("Status:", order[6])

        print("\nItems:")

        # Display all items in same order
        for item in orders:

            if item[0] == order_id:

                print("-", item[1], "x" + item[2])


# =========================================================
# Check stock availability
# =========================================================
def check_stock(menu, item_name, qty):

    for item in menu:

        # Compare FULL item name
        if item[1].lower() == item_name.lower():

            stock = int(item[3])

            if qty <= stock:
                return True

            else:
                return False

    return False


# =========================================================
# Reduce stock
# =========================================================
def reduce_stock(menu, item_name, qty):

    for item in menu:

        # Compare FULL item name
        if item[1].lower() == item_name.lower():

            current_stock = int(item[3])

            new_stock = current_stock - int(qty)

            item[3] = str(new_stock)

            break


# =========================================================
# Restore stock
# =========================================================
def restore_stock(menu, item_name, qty):

    for item in menu:

        # Compare FULL item name
        if item[1].lower() == item_name.lower():

            current_stock = int(item[3])

            new_stock = current_stock + int(qty)

            item[3] = str(new_stock)

            break


# =========================================================
# Update grouped order status
# =========================================================
def update_order_status(): 

    orders = load_orders()
    menu = load_menu()

    display_orders()

    order_id = input("\nEnter Order ID: ")

    found = False

    print("\n1. pending")
    print("2. accepted")
    print("3. cancelled")

    status = input("Enter choice: ")

    for order in orders:

        # Find all items in same order
        if order[0] == order_id:

            found = True

            item_name = order[1]
            qty = int(order[2])

            old_status = order[6]

            # =====================================================
            # PENDING
            # =====================================================
            if status == "1":

                order[6] = "pending"

                # Restore stock if previously accepted
                if old_status == "accepted":

                    restore_stock(menu, item_name, qty)

            # =====================================================
            # ACCEPTED
            # =====================================================
            elif status == "2":

                # Prevent double deduction
                if old_status != "accepted":

                    # Check stock before reducing
                    if check_stock(menu, item_name, qty):

                        reduce_stock(menu, item_name, qty)

                        order[6] = "accepted"

                    else:

                        print("\nNot enough stock for:", item_name)

                        order[6] = "cancelled"

                else:
                    print("\nOrder already accepted.")

            # =====================================================
            # CANCELLED
            # =====================================================
            elif status == "3":

                order[6] = "cancelled"

                # Restore stock if previously accepted
                if old_status == "accepted":

                    restore_stock(menu, item_name, qty)

            else:
                print("Invalid input.")
                return

    if not found:
        print("Order ID not found.")
        return

    # Save updated data
    save_orders(orders)
    save_menu(menu)

    print("\nOrder updated successfully.")





#----------------------------------------- Customer Side --------------------------------------




# =========================================================
# Place customer order
# =========================================================
def place_order():

    menu = load_menu()
    orders = load_orders()

    print("\n===== PLACE ORDER =====")

    customer_name = input("Enter your name: ")
    address = input("Enter your address: ")
    contact = input("Enter your contact number: ")

    # Generate new order ID
    if len(orders) == 0:
        order_id = 1

    else:
        last_order = orders[-1]
        order_id = int(last_order[0]) + 1

    cart = []

    while True:

        # Show menu
        display_menu()

        choice = input("\nSelect item number: ")

        if not choice.isdigit():
            print("Invalid input.")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(menu):
            print("Invalid item number.")
            continue

        selected_item = menu[choice - 1]

        item_name = selected_item[1]
        stock = int(selected_item[3])

        # Prevent ordering unavailable items
        if stock <= 0:
            print("Item is OUT OF STOCK.")
            continue

        qty = input("Enter quantity: ")

        if not qty.isdigit():
            print("Invalid quantity.")
            continue

        qty = int(qty)

        # Check stock
        if qty > stock:
            print("Not enough stock.")
            continue

        # Add item into cart
        cart.append([
            str(order_id),
            item_name,
            str(qty),
            customer_name,
            address,
            contact,
            "pending"
        ])

        print(item_name, "added to order.")

        again = input("Add another item? (Y/N): ")

        if again.upper() != "Y":
            break

    # Save all order rows
    if len(cart) > 0:

        print("\n===== ORDER SUMMARY =====")

        for item in cart:

            print("-", item[1], "x" + item[2])

        confirm = input("\nConfirm order? (Y/N): ")

        if confirm.upper() == "Y":

            orders.extend(cart)

            save_orders(orders)

            print("Order placed successfully.")
            print("Your Order ID is:", order_id)

        else:
            print("Order cancelled.")

    else:
        print("No items selected.")


# =========================================================
# View customer order history
# =========================================================
def view_order_history():

    orders = load_orders()

    customer_name = input("\nEnter your name: ").lower()

    found = False
    shown_orders = []

    print("\n===== ORDER HISTORY =====")

    for order in orders:

        order_id = order[0]

        # Skip displayed orders
        if order_id in shown_orders:
            continue

        # Match customer name
        if order[3].lower() == customer_name:

            shown_orders.append(order_id)

            found = True

            print(f"\nOrder ID: {order_id}")

            print("Address:", order[4])
            print("Contact:", order[5])
            print("Status:", order[6])

            print("\nItems:")

            # Show all items in same order
            for item in orders:

                if item[0] == order_id:

                    print("-", item[1], "x" + item[2])

    if not found:
        print("No orders found.")

