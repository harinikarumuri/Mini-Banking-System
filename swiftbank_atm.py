# Mini Bank Management System - SwiftBank

# Sample user database (username: password)
users = {
    "Harini": {"password": "1234", "balance": 5000},
    "Harshitha": {"password": "abcd", "balance": 3000}
}

# Function to authenticate user
def login():
    print("==== Welcome to SwiftBank ====")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username]["password"] == password:
        print(f"Login successful! Welcome, {username.capitalize()}!\n")
        return username
    else:
        print("Invalid credentials. Try again.\n")
        return None

# Function to display menu
def show_menu():
    print("----- SwiftBank Main Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# Function to check balance
def check_balance(user):
    balance = users[user]["balance"]
    print(f"Your current balance is: ₹{balance}\n")

# Function to deposit money
def deposit(user):
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        users[user]["balance"] += amount
        print(f"₹{amount} deposited successfully.\n")
    else:
        print("Invalid amount.\n")

# Function to withdraw money
def withdraw(user):
    amount = float(input("Enter amount to withdraw: ₹"))
    if 0 < amount <= users[user]["balance"]:
        users[user]["balance"] -= amount
        print(f"₹{amount} withdrawn successfully.\n")
    else:
        print("Insufficient balance or invalid amount.\n")

# Main Program
def main():
    user = None
    while not user:
        user = login()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(user)
        elif choice == "2":
            deposit(user)
        elif choice == "3":
            withdraw(user)
        elif choice == "4":
            print("Thank you for banking with SwiftBank. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the program
main()