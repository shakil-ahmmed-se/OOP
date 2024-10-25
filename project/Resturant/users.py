from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email 
        self.address = address


class Customer(User):
    def __init__(self, name,phone, email, address, money,) -> None:
        self.wallet = money
        self.__order = None
        self.due_amount = 0
        super().__init__(name, phone, email, address)

    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        self.due_amount += order.bill
        print(f'{self.name} place and order with bill: {order.bill}')

    def eat_food(self, order):
        print(f'{self.name} eating food {order.items}')

    def pay_for_oder(self, amount):
        #to do : submit the money to manager

        pass

    def give_tips(self,tips_amount):
        pass

    def writes_review(self, stars):
        pass

class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_job_date, department, ) -> None:
        self.salary = salary
        self.due = salary
        self.starting_job_date = starting_job_date
        self.department = department
        super().__init__(name,phone, email, address)
    
    def recive_salary(self):
        self.due = 0

class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_job_date, department, cooking_item) -> None:
        self.cooking_item = cooking_item

        super().__init__(name, phone, email, address, salary, starting_job_date, department)

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_job_date, department) -> None:
        self.tips_earn = 0
        super().__init__(name, phone, email, address, salary, starting_job_date, department)

    def take_order(self,order):
        pass

    def transfer_order(self, order):
        pass

    def serve_food(self,order):
        pass

    def revice_tips(self, amount):
        self.tips_earn += amount


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_job_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_job_date, department)