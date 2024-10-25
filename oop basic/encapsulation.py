# Encapsulation = hide all implementation details

class Bank:
    def __init__(self, holder_name, initial_deposite) -> None:
        self.holder_name = holder_name      # public
        self._branch = 'Banani 11'          # protected
        self.__balance = initial_deposite   # private

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'You dont have enough balace'

rafSun = Bank('Choto broo',10000)
print(rafSun.holder_name)
rafSun.holder_name = 'Boro Bhai'
rafSun.deposite(5000)
print(rafSun.get_balance())
print(rafSun.holder_name)
print(rafSun._branch)
# print(dir(rafSun))
print(rafSun._Bank__balance)
