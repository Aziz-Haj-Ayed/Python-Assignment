#MOHAMED AZIZ HAJ AYED
#TP148576


#Link with other classes
from customer_menu import customer_menu
from login import staff_login


# =========================================================
# Displays the main welcome menu of the system.
# =========================================================
def main_menu():

    while True:

        print("\n===================================")
        print("   CAFE ORDER TRACKING SYSTEM")
        print("===================================")

        print("1. Continue as Customer")
        print("2. Staff Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_menu()

        elif choice == "2":
            staff_login()

        elif choice == "3":
            print("\nSee you next time.")
            break

        else:
            print("Invalid choice. Please try again.")


main_menu()