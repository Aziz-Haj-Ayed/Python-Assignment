from menu_storage import *

# Displays customer menu options.
# =========================================================
def customer_menu():

    while True:

        print("\n===== CUSTOMER MENU =====")

        print("1. View Menu")
        print("2. Search Item")
        print("3. Place Order")
        print("4. View Order History")
        print("5. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            search_item()

        elif choice == "3":
            place_order()

        elif choice == "4":
            view_order_history()

        elif choice == "5":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice.")