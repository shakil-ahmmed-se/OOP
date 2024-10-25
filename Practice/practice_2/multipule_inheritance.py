class Company:
    def __init__(self,cname,location) -> None:
        self.cname = cname
        self.location = location
    def company_tails(self):
        print(f'Companay Details : {self.cname} location : {self.location}')

class Person:
    def __init__(self,pname, age) -> None:
        self.pname =pname
        self.age = age

    def person_details(self):
        print(f'Person Name : {self.pname} and age {self.age}')


class Employee(Company,Person):
    def __init__(self,em_name,em_age , cmp_name, cmp_location) -> None:
        Person.__init__(self,em_name,em_age)
        Company.__init__(self,cmp_name,cmp_location)
        
obj_employee = Employee('Jamal',29,'Microsoft','California')
obj_employee.person_details()
obj_employee.company_tails()