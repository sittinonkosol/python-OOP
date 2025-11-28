class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    @property
    def owner(self):
        return self.__owner
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'deposit successful')
        else:
            print(f'deposit failed')
        
    def withdraw(self, amount):
        if amount <= 0:
            print('amount must be greater than zero')
        elif amount > self.__balance:
            print('not enough balance')
        else:
            self.__balance -= amount
            print(f'withdraw {amount} successful')

    def __str__(self):
        return f'BankAccount(owner={self.owner}, balance={self.balance})'

acc1 = BankAccount('Non', 1000)
print(acc1)
acc1.deposit(500)
acc1.withdraw(200)
print("Balance:", acc1.balance)