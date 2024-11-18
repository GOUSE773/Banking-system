
import datetime


class Account:
    """A class to represent a bank account."""

    def __init__(self, name, account_number, initial_balance=0.0):
        """Initialize account with a holder's name, number, and initial balance."""
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []  # To store the history of transactions

        # Record account creation
        self.transactions.append(f"Account created on {datetime.datetime.now()} with balance {self.balance:.2f}")

    def deposit(self, amount):
        """Deposit money to the account."""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount:.2f} on {datetime.datetime.now()}")
            print(f"Successfully deposited {amount:.2f}. Current balance: {self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Withdrawn: {amount:.2f} on {datetime.datetime.now()}")
                print(f"Successfully withdrawn {amount:.2f}. Current balance: {self.balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        """Display the current balance."""
        print(f"Current balance: {self.balance:.2f}")
        return self.balance

    def get_transaction_history(self):
        """Display the transaction history."""
        print("\n--- Transaction History ---")
        if self.transactions:
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions available.")


class Bank:
    """A class to manage multiple bank accounts."""

    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0.0):
        """Create a new bank account."""
        account_number = len(self.accounts) + 1
        new_account = Account(name, account_number, initial_balance)
        self.accounts[account_number] = new_account
        print(f"Account created successfully. Your account number is {account_number}.")

    def access_account(self, account_number):
        """Access an existing bank account."""
        return self.accounts.get(account_number, None)


def main():
    """Main function to run the banking system."""
    bank = Bank()
    print("\nWelcome to Python Bank System!")

    while True:
        print("\n1. Create New Account")
        print("2. Access Existing Account")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter your name: ")
            try:
                initial_balance = float(input("Enter initial deposit amount: "))
            except ValueError:
                print("Invalid amount entered.")
                continue
            bank.create_account(name, initial_balance)

        elif choice == 2:
            try:
                account_number = int(input("Enter your account number: "))
            except ValueError:
                print("Invalid account number.")
                continue

            account = bank.access_account(account_number)

            if account:
                while True:
                    print("\n1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Logout")

                    try:
                        sub_choice = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    if sub_choice == 1:
                        try:
                            deposit_amount = float(input("Enter amount to deposit: "))
                        except ValueError:
                            print("Invalid amount entered.")
                            continue
                        account.deposit(deposit_amount)

                    elif sub_choice == 2:
                        try:
                            withdraw_amount = float(input("Enter amount to withdraw: "))
                        except ValueError:
                            print("Invalid amount entered.")
                            continue
                        account.withdraw(withdraw_amount)

                    elif sub_choice == 3:
                        account.get_balance()

                    elif sub_choice == 4:
                        account.get_transaction_history()

                    elif sub_choice == 5:
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Account not found. Please check your account number.")

        elif choice == 3:
            print("Thank you for using Python Bank System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


    
