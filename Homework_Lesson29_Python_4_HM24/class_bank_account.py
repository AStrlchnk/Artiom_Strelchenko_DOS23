class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"The account {self.account_number} has been funded with {amount}. New balance: {self.balance}")
        else:
            print("The amount for replenishment must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Account {amount} withdrawal {self.account_number}. Balance: {self.balance}")
            else:
                print("Insufficient funds in the account.")
        else:
            print("The amount for replenishment must be positive.")

    def __str__(self):
        return f"Account {self.account_number}, Owner: {self.owner_name}, Balance: {self.balance}"

account1 = BankAccount("123456", "Ivan Semin", 1000)
account2 = BankAccount("654321", "Natalia Lukina", 500)
account3 = BankAccount("789123", "Alexander Ivanov")

print(account1)
account1.deposit(500)
account1.withdraw(300)

print()

print(account2)
account2.deposit(200)
account2.withdraw(800)

print()

print(account3)
account3.deposit(1000)
account3.withdraw(1500)