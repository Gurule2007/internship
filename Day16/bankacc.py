class Bankaccount:
    def __init__(self, acc_holder):
        self.acc_holder = acc_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print(f"Account holder: {self.acc_holder}")
        print(f"Current balance: {self.balance}")

B = Bankaccount("Aditya Gurule")
B.deposit(1000)
B.withdraw(500)
B.display_balance()



