class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Balance: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount:.2f}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn: ${amount:.2f}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

# Simplified ATM simulation
atm = ATM()

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        print(atm.check_balance())
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        print(atm.deposit(amount))
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        print(atm.withdraw(amount))
    elif choice == "4":
        print("Thank you. Visit again!")
        break
    else:
        print("Invalid choice. Enter a number between 1 and 4.")
