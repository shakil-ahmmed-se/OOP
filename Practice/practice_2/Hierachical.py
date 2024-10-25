class Studen:
    def __init__(self, name , id) -> None:
        self.name = name
        self.__id = id
    def details(self):
        print(f'Name : {self.name} id : {self.__id}')

ob = Studen('Joshim',25)
print('Before Change')
ob.details()

print('after change')
ob.__id = 0
ob.details()