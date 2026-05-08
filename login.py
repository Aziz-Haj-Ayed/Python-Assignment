import csv
from staff_menu import staff_menu


# =========================================================
# Loads username and password data from CSV file.
# =========================================================
def load_staff_data():

    staff_accounts = {}

    try:
        with open("Staff_Data.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if len(row) >= 2:

                    username = row[0]
                    password = row[1]

                    staff_accounts[username] = password

    except FileNotFoundError:
        print("ERROR: Stuff_Data.csv file not found.")

    return staff_accounts


# =========================================================
# Allows staff members to login.
# =========================================================
def staff_login():

    staff_accounts = load_staff_data()

    print("\n===== STAFF LOGIN =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in staff_accounts:

        if staff_accounts[username] == password:

            print(f"\nWelcome, {username}!")
            staff_menu()

        else:
            print("Incorrect password.")

    else:
        print("Username not found.")