from abc import ABC ,abstractmethod

class Animal(ABC):
    @abstractmethod         # enforce to all derived class to have a eat method
    def eat(self):
        print('I need Food')

    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.cetagory = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('Hey na Nana, Eating Banana')

layka = Monkey('Lucky')
layka.eat()
print()