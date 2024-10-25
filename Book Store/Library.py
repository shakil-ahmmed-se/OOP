class Book:
    def __init__(self, id, name, quantity) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity


class User:
    def __init__(self,id, name,password) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.borrowedBook = []
        self.returnBook = []

class Library:
    def __init__(self,name) -> None:
        self.name = name
        self.users = []
        self.books = []

    def add_books(self,id, name,  quantity):
        for book in self.books:
            if book.id==id:
                print(f"\n\t---> !! Book Id {book.id} already exists")
                return
            
        book = Book(id, name, quantity)
        self.books.append(book)
        print(f'{book.name} add successfully')
    
    def add_users(self,id, name , password):
        user = User(id, name, password)
        self.users.append(user)
        return user
    
    def borrow_book(self, user, token):
        for book in self.books:
            if book.id == token:
                if book in user.borrowedBook:
                    print('Already borrow the book')
                    return
                elif book.quantity == 0:
                    print('No copy avaible')
                    return
                else:
                    user.borrowedBook.append(book)
                    book.quantity -= 1
                    print(f'Borrow {book.name} successfully')
                    return
        print(f'Not found any book with id : {token}')
    
    def return_book(self,user, token):
        for book in self.books:
            if book.id==token:
                if book in user.borrowedBook:
                    book.quantity += 1
                    user.returnBook.append(book)
                    user.borrowedBook.remove(book)
                    print(f'Return {book.name} book successfully')
                    return
                else:
                    print(f'You are not reading {book.name} now')
                    return
            
        print(f'Not found any book with id : {token}')
        
boi = Library('Bichitra Boi')
admin = boi.add_users(100,'admin', 'admin')
rakib = boi.add_users(17,'rakib','123')
cpbook = boi.add_books(15,'bangla',5)

currentUser = admin

while True:
    if currentUser==None:
        print("\n\t--->!!! No logged in user\n")
        
        option=input("Login or Register (L/R) :")

        if option == 'L':
            id = int(input('Enter Id :'))
            password = input('Enter password: ')

            match = False
            for user in boi.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    match = True
                    break
            if match == False:
                print('No user found')
        elif option == 'R':
            id = int(input('Enter id'))
            name = input('Enter your name')
            password = input('Enter a password')

            for user in boi.users:
                if user.id == id:
                    print('User already exsist')
                
            user = boi.add_users(id,name,password)
            currentUser = user
    else:
        print('\n')
        print(f'Welcome back {currentUser.name} \n')
        if currentUser.name == 'admin':
            print('option \n')
            print('1: Add book')
            print('2: Add user')
            print('3: Show all books')
            print('4: LogOut')

            ch = int(input('Enter option'))
            print('\n')
            
            if ch == 1:
                id = int(input('Enter book id'))
                name = input('Enter book name ')
                quant = int(input('Enter book quantity'))

                boi.add_books(id,name,quant)

            elif ch == 3:
                for book in boi.books:
                    print(f'{book.id} {book.name} {book.quantity}')
                    # print('\n')
            
            elif ch == 4:
                currentUser = None
        
        else:
            print('option \n')
            print('1: Borrow Book')
            print('2: Return Book')
            print('3: Show Borrow all books')
            print('4: Show History')
            print('5: LogOut')

            ch = int(input('Enter option'))

            if ch == 1:
                id = int(input())
                boi.borrow_book(currentUser,id)
            elif ch == 2:
                id = int(input())
                boi.return_book(currentUser,id)

            elif ch == 3:
                print('All borrow book')

                for book in currentUser.borrowedBook:
                    print(f'{book.id} {book.name}  {book.quantity}')
                    
            elif ch == 4:
                print('History : ')

                for book in currentUser.returnBook:
                    print(f'{book.id} {book.name}  {book.quantity}')

            elif ch == 5:
                currentUser = None
                    






