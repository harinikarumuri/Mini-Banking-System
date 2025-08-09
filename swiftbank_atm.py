# swiftbank_atm.py

# Sample user data: username -> [PIN, balance]
users = {
    "harshitha": ["1234", 5000],
    "deepthi": ["5678", 10000]
}

def authenticate():
    print("Welcome to SwiftBank ATM")
    username = input("Enter your username: ")
    pin = input("Enter your PIN: ")

    if username in users and users[username][0] == pin:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials. Try again.")
        return None

def show_menu():
    print("\nPlease choose an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance(user):
    print(f"Your current balance is ₹{users[user][1]}")

def deposit(user):
    amount = float(input("Enter amount to deposit: ₹"))
    users[user][1] += amount
    print(f"₹{amount} deposited successfully.")

def withdraw(user):
    amount = float(input("Enter amount to withdraw: ₹"))
    if users[user][1] >= amount:
        users[user][1] -= amount
        print(f"₹{amount} withdrawn successfully.")
    else:
        print("Insufficient balance.")

def main():
    user = None
    while not user:
        user = authenticate()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(user)
        elif choice == "2":
            deposit(user)
        elif choice == "3":
            withdraw(user)
        elif choice == "4":
            print("Thank you for using SwiftBank ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
