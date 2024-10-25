class bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 100000
    def get_balace(self):
        return self.balance
    
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'You can not withdraw under {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'You can not withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is you money {amount}')
            print(f'Your balance after withdraw {self.get_balace()}')

brac = bank(150000)
brac.withdraw(20)
brac.withdraw(50000000)
brac.withdraw(50000)

    
