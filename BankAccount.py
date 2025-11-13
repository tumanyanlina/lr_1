class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Зачисление: +{amount}р Ваш баланс: {self.balance}р")
    
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Покупка: {amount}р Ваш баланс: {self.balance}р")
        else:
            print(f"Недостаточно средств. Покупка {amount}р")
    
    def check_balance(self):
        print(f"Ваш баланс: {self.balance}р")
        return self.balance

print("Создание нового счета")
my_account = BankAccount(5000)
my_account.check_balance()

print("\nПополнение счета")
my_account.deposit(500)    
my_account.deposit(200)   

print("\nСнятие денежных средств со счета")
my_account.withdrawal(300)   
my_account.withdrawal(1500)
my_account.withdrawal(5000)
print("\n")
my_account.check_balance()