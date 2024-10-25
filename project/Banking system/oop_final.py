from abc import ABC,abstractmethod
import random

class Bank:
    account_list= []
    users = []
        # self.name = name
    total_balance = 0
    totalLoan = 0
    loan_status = True
        
    isbankrupt = True

    def total_bank_balance(self):
        for account in Bank.account_list:
            Bank.total_balance += account.balance 
        print(f'Total balance of Bank: {Bank.total_balance}')

    
    def create_account(self,name, email,account_number,account_type,address):
        user = User( name, email,account_number,account_type,address)
        Bank.account_list.append(user)
        

    def delete_account(self, account_number):
        for account in  Bank.account_list:
            if account.account_number == account_number:
                Bank.account_list.remove(account)
                # self.account_list.remove(account)
                print('Account deleted successfully')
                return
        print('Account not found')

    def show_users(self):
        for account in Bank.account_list:
            print(f'Account Number : {account.account_number} Name :{account.name} Email: {account.email}')

    def total_bank_Loan(self):
        print(f'Total Bank Loan {Bank.totalLoan}')
        
    def enable_loan(self):
        Bank.loan_status = True
        print('Loan Status Enabled')
    def disable_loan(self):
        Bank.loan_status = False
        print('Loan Status Disabled')

class User(ABC):
    # accounts = []

    def __init__(self, name, email,account_number,account_type,address) -> None:
        self.name = name
        self.email = email
        self.account_number = account_number
        self.account_type = account_type
        self.address = address
        self.transictions = []
        self.balance = 0
        self.loan_limit = 2
        self.total_loan = 0

        Bank.account_list.append(self)
        # Bank.users.append(self)

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f'\n {amount} deposit successful \n')
            self.transictions.append(f'Deposit: {amount}')
        else:
            print('\n Invalid Amount')
    
    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            self.transictions.append(f'Withdraw: {amount}')
            print(f'{amount} withdraw successfully')
        
        else:
            print('\n Withdrawal amount exceeded')

    @abstractmethod
    def available_balance(self):
        pass
    
    @abstractmethod
    def show_info(self):
        pass
   
    def transaction_history(self):
        for transaction in self.transictions:
            print(transaction)
        
    def transfer_amount(self, other_account, amount):
        if amount >= 0 and amount <= self.balance:
            for account in Bank.account_list:
                if  other_account == account.account_number:
                    self.balance -= amount
                    account.balance += amount
                    self.transictions.append(f'Send {amount} ot {other_account}')
                    # account.transictions.append(f'Received {amount} to {self.account_number}')
                    print('\nTransfer Amount Successful')
                    return
            else:
                print('\n Account does not exist')
        else:
            print('\n Invalid amount or insufficient balance')
                

    def take_loan(self,amount):
        if amount>= 0 and self.loan_limit <= 2:
            self.balance += amount
            self.transictions.append(f'Loan taken: {amount}')
            self.loan_limit -=1
            self.total_loan += amount
            Bank.totalLoan += amount
            # Bank.total_bank_Loan(self,amount)
            print(f'\nTake :{amount} Loan Successful')
        else:
            print(f'\nInvalid amount or limit over')

class SavingsAccount(User):
    def __init__(self, name, email, account_number,interestRate, address) -> None:
        self.interestRate = interestRate
        # self.limit_transfer = limit_transfer
        super().__init__(name, email, account_number, 'savings', address)

    def available_balance(self):
        print(f'Available Balance Saving account: {self.balance}')
    
    def applyInterest(self):
        interest = self.balance * (self.interestRate / 100)
        print(f'Interest Applied {interest}')
        self.deposit(interest)

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance and amount <= 2500000:
            self.balance -= amount
            print(f'{amount} withdraw successfully')
        
        else:
            print('\n Withdrawal amount exceeded')

    def show_info(self):
        print(f'Show information of {self.name}')
        print(f'\nAccount Number : {self.account_number}')
        print(f'Current Balance: {self.balance}')
        print(f'Account Type {self.account_type}')
    
class CurrentAccount(User):
    def __init__(self, name, email, account_number, address) -> None:
        super().__init__(name, email, account_number, 'current', address)

    def available_balance(self):
        print(f'Available Balance of Current Account: {self.balance}')
    
    def show_info(self):
        print(f'Show information of {self.name}')
        print(f'\nAccount Number : {self.account_number}')
        print(f'Current Balance: {self.balance}')
        print(f'Account Type {self.account_type}')

currentuser = None

while True:
    if currentuser == None:
        print('No Users loggIn\n')
        print('1.Login as Admin(admin): \n')
        print('2.Create Account or LogIn(C/L): \n')
        choise = int(input('Enter Choise: '))
        if choise == 1:
            nm = input('Enter admin name(admin): ')
            if nm == 'admin':
                currentuser = 'admin'
                continue
        elif choise == 2:
            ch = input('Create Account or LogIn(C/L): \n')
        else:
            print('Wrong Type: ')
            
        if ch == 'C':
            name = input('Enter your name: ')
            eml = input('Enter your email: ')
           
            accNumber = random.randint(1000000,999999999)
            addr = input('Enter your address: ')
            accType = input('Account Type(sv= savings/cr = Current): (sv/cr)')
            if accType == 'sv':
                irate = int(input('Interest Rate: '))
                currentuser = SavingsAccount(name,eml,accNumber,irate,addr)
                

            elif accType == 'cr':
                currentuser = CurrentAccount(name,eml,accNumber,addr)
            
            else:
                print('Invalid Account Type: ')
        
        elif ch == 'L':
            num = int(input('Enter your account number: '))

            for account in Bank.account_list:
                if num == account.account_number:
                    currentuser = account
                    break
                else:
                    print(f'\n{num} account not found')
        
        else:
            print('Invalid Type: ')
        
    else:
        
        if currentuser == 'admin':
            print(f'\n Welcome {currentuser}\n')
            print('1: Create Account        : ')
            print('2: Deleted Account       : ')
            print('3: Show all Users        : ')
            print('4: Total Bank Balance    : ')
            print('5: Total Loan Amount     : ')
            print('6: Loan featur (on/ off) : ')
            print('7: LogOut : ')

            op = int(input('Enter Option: '))

            if op == 1:
                name = input('Enter your name: ')
                eml = input('Enter your email: ')
                accNumber = random.randint(1000000,999999999)
                addr = input('Enter your address: ')
                accType = input('Account Type(sv= savings/cr = Current): (sv/cr)')
                if accType == 'sv':
                    irate = int(input('Interest Rate: '))
                    currentuser = SavingsAccount(name,eml,accNumber,irate,addr)
                    Bank.account_list.append(currentuser)

                elif accType == 'cr':
                    currentuser = CurrentAccount(name,eml,accNumber,addr)
                    Bank.account_list.append(currentuser)
                else:
                    print('Invalid Account Type: ')
                
            elif op == 2:
                accNumber = int(input('Enter account number: '))
                Bank.delete_account(currentuser,accNumber)
            
            elif op == 3:
                Bank.show_users(currentuser)

            elif op == 4:
                Bank.total_bank_balance(currentuser)

            elif op == 5:
                Bank.total_bank_Loan(currentuser)
            
            elif op == 6:
                feature = input('Enter choise(on/off)')
                if feature == 'on':
                    Bank.enable_loan(currentuser)
                elif feature == 'off':
                    Bank.disable_loan(currentuser)
                else:
                    print('\nInvalid Option')
            
            elif op == 7:
                currentuser = None
          

        else:
            print(f'\n Welcome {currentuser.name}\n')

            if currentuser.account_type == 'savings':
                print('1. Show Info          : ')
                print('2. Deposit            : ')
                print('3. Withdraw           : ')
                print('4. Apply Interest     : ')
                print('5. Balance            : ')
                print('6. Transaction History: ')
                print('7. Take Loan          : ')
                print('8. Transfer Amount    : ')
                print('9. LogOut             : ')

                op = int(input('\nEnter Option : '))
                if op == 1:
                    currentuser.show_info()
                elif op == 2:
                    amount = int(input('Enter Deposit Amount: '))
                    currentuser.deposit(amount)
                
                elif op ==3:
                    amount = int(input('Enter Withdraw Amount: '))
                    currentuser.withdraw(amount)
                
                elif op == 4:
                    currentuser.applyInterest()
                
                elif op == 5:
                    currentuser.available_balance()

                elif op == 6:
                    currentuser.transaction_history()
                
                elif op == 7:
                    amount = int(input('Enter Amount of Loan: '))
                    # Bank.total_bank_Loan(amount)
                    currentuser.take_loan(amount)
                elif op == 8:
                    accNum = int(input('Enter Receiver Account Number: '))
                    amount = int(input('Enter Trasfer Amount : '))
                    currentuser.transfer_amount(accNum,amount)
                
                elif op == 9:
                    currentuser = None
            
            else:
                if currentuser.account_type == 'current':
                    print('1. Show Info          : ')
                    print('2. Deposit            : ')
                    print('3. Withdraw           : ')
                    print('4. Balance            : ')
                    print('5. Transaction History: ')
                    print('6. Take Loan          : ')
                    print('7. Transfer Amount    : ')
                    print('8. LogOut             : ')

                    op = int(input('\nEnter Option : '))
                    if op == 1:
                        currentuser.show_info()
                    elif op == 2:
                        amount = int(input('Enter Deposit Amount: '))
                        currentuser.deposit(amount)
                    
                    elif op ==3:
                        amount = int(input('Enter Withdraw Amount: '))
                        currentuser.withdraw(amount)
                    
                    elif op == 4:
                        currentuser.available_balance()

                    elif op == 5:
                        currentuser.transaction_history()
                    
                    elif op == 6:
                        amount = int(input('Enter Amount of Loan: '))
                        # Bank.total_bank_Loan(amount)
                        currentuser.take_loan(amount)
                    elif op == 7:
                        accNum = int(input('Enter Receiver Account Number: '))
                        amount = int(input('Enter Trasfer Amount : '))
                        currentuser.transfer_amount(accNum,amount)
                    
                    elif op == 8:
                        currentuser = None
                    
