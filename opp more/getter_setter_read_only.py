class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    #getter without any setter is read only attribute
    @property
    def age(self):
        return self._age

    #getter
    @property
    def salary(self):
        return self.__money
    
    #setter
    @salary.setter
    def salary(self,value):
        if value < 0 :
            return 'Salary can not be negative'
        else:
            self.__money += value

samsu = User('Kopa', 21, 12000)
# print(samsu.age())
print(samsu.age) # jodi @property use kori 

# print(samsu.salary())
print(samsu.salary)
samsu.salary = 4500
print(samsu.salary)