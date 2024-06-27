# Encapsulation
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

# Polymorphism
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)

# Using polymorphism
savings_acc = SavingsAccount("SA001", 1000, 5)
savings_acc.deposit(500)
print(savings_acc.balance)  # Output: 1500
