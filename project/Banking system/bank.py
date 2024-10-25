from abc import ABC,abstractmethod
import random

class Account(ABC):
    accounts = []

    def __init__(self, name, account_number, password, account_type) -> None:
        self.name = name 
        self.account_number = account_number
        self.password = password
        self.account_type = account_type

        self.balance  = 0

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print('\n Deposit Successful')
        else:
            print(f'{amount} Amount not able to Deposit:')

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            print('\n Withdraw Successful')
        else:
            print('\nInvalid Amount')

    def changeInfo(self,name):
        self.name = name
    
    #over loading of method changeinfo
    def changeInfo(self,name,password):
        self.name = name
        self.password = password
        print('\n Information Changed \n')

    @abstractmethod
    def showInfo(self):
        pass


class SavingsAccount(Account):
    def __init__(self, name, account_number, password, interestRate) -> None:
        self.interestRate = interestRate
        super().__init__(name, account_number, password, 'savings')

    def showInfo(self):
        print(f'\n Showing Info of {self.name}')
        print(f'\n Account Number {self.account_number}')
        print(f'\n Account Type {self.account_type}')
        print(f'\n Balance {self.balance}')

    def applyInterest(self):
        interest = self.balance * (self.interestRate / 100)
        print(f'Interest Applied {interest}')
        self.deposit(interest)

    
class SpecialAcount(Account):
    def __init__(self, name, account_number, password, limit) -> None:
        self.limit = limit
        super().__init__(name, account_number, password, 'special')

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.limit:
            self.balance -= amount
            print('\n Withdraw Successful(sp)')
        else:
            print('\n Invalid Amount')
    
    def showInfo(self):
        print(f'\n Showing Info {self.account_type} of {self.name}')
        print(f'\n Account Number {self.account_number}')
        print(f'\n Balance {self.balance}')


currentuser = None

while True:
    if currentuser == None:
        print('\n No Users Loggin\n')
        ch = input('LogIn or Register(L/R)')
        if ch == 'R':
            name = input('Enter your Name: ')
            nu = random.randint(1000000,1000000000)
            pa = input('Enter Password : ')
            acc_type = input('Account Type: (sv/sp)')
            if acc_type == 'sv':
                irate = int(input('Interest Rate: '))
                currentuser = SavingsAccount(name,nu,pa,irate)
                Account.accounts.append(currentuser)
            elif acc_type == 'sp':
                lim = int(input('Enter limitation: '))
                currentuser = SpecialAcount(name,nu,pa,lim)
                Account.accounts.append(currentuser)
            else:
                print('\nInvalid Choise\n')
            
        elif ch == 'L':
            no =int(input('Enter Account Number: '))
            
            for account in Account.accounts:
                if no == account.account_number:
                    currentuser = account
                    break
        else:
            print('\nInvalid Type\n')
        
    else:
        print(f'\n Welcome {currentuser.name}\n')

        if currentuser.account_type == 'savings':
            print('1. Show Info ')
            print('2. Deposit  ')
            print('3. Withdraw ')
            print('4. Apply Interest ')
            print('5. Change Info')
            print('6. LogOut ')

            op = int(input('Enter Option : '))

            if op == 1:
                currentuser.showInfo()

            elif op == 2:
                amount = int(input('Enter amount : '))
                currentuser.deposit(amount)

            elif op == 3:
                amount = int(input('Enter amount : '))
                currentuser.withdraw(amount)

            elif op == 4:
                currentuser.applyInterest()

            elif op == 5:
                name = input('Enter new name : ')
                pa = input('Enter new password : ')

                currentuser.changeInfo(name,pa)
            
            elif op == 6:
                currentuser = None

        else:
            print('1. Show Info ')
            print('2. Deposit  ')
            print('3. Withdraw ')
            print('4. Change Info')
            print('5. LogOut ')

            op = int(input('Enter Option : '))

            if op == 1:
                currentuser.showInfo()

            elif op == 2:
                amount = int(input('Enter amount : '))
                currentuser.deposit(amount)

            elif op == 3:
                amount = int(input('Enter amount : '))
                currentuser.withdraw(amount)
            elif op == 4:
                name = input('Enter new name : ')
                pa = input('Enter new password : ')

                currentuser.changeInfo(name,pa)
            
            elif op == 5:
                currentuser = None
            



    