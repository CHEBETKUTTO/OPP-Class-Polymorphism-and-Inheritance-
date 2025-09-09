# Parent Class
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance  # Private attribute (Encapsulation)

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.owner} deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def account_type(self):
        return "Generic Bank Account"


# Child Class 1 - Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    # Method specific to SavingsAccount
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} added.")

    # Overriding method (Polymorphism)
    def account_type(self):
        return "Savings Account"


# Child Class 2 - Checking Account
class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=100):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    # Overriding withdraw method to allow overdraft
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            # accessing balance indirectly through deposit/withdraw
            new_balance = self.get_balance() - amount
            if new_balance < 0:
                print(f"Overdraft used! Balance went below 0.")
            super().withdraw(amount)
        else:
            print("Amount exceeds overdraft limit.")

    # Overriding method (Polymorphism)
    def account_type(self):
        return "Checking Account"


# -----------------------------
# Example Usage
# -----------------------------

savings = SavingsAccount("S001", "Linda", 5000, interest_rate=0.05)
checking = CheckingAccount("C001", "Alex", 200, overdraft_limit=300)

print(savings.account_type())   # Savings Account
print(checking.account_type())  # Checking Account

savings.deposit(1000)
savings.add_interest()

checking.withdraw(400)  # Uses overdraft
checking.deposit(200)
