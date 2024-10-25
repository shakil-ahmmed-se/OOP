class Animal:
    def __init__(self, name) -> None:
        self.name = name
    def eat(self):
        print(self.name, 'can eat')

class Cat(Animal):
    def speak(self):
        print('meow meow')

class Dog(Animal):
    def speak(self):
        print('Gheu Gheu')

cat = Cat('Cat')
cat.eat()
dog = Dog('Dog')
dog.eat()