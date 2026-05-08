from menu_storage import *



# Displays staff menu options.
# =========================================================
def staff_menu():

    while True:

        print("\n===== STAFF MENU =====")

        print("1. View Menu")
        print("2. Search Item By Key Word")
        print("3. Add Item")
        print("4. Update Item")
        print("5. Confirm Orders")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            search_item()

        elif choice == "3":
            add_item()

        elif choice == "4":
            update_menu_item()

        elif choice == "5":
            update_order_status()

        elif choice == "6":
            print("Logging out...")
            break

        else:
            print("Invalid choice.")