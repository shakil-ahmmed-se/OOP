# poly = many (multipule)
# morphism = shape

class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def make_sound(self):
        print('Animal making some sound ')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('Meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Gheu Gheu ')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('Greatest Of All Time')


don = Cat('Real Done')
don.make_sound()
dog = Dog('Separd')
dog.make_sound()

mess = Goat('Messi')
mess.make_sound()

less = Goat('Nymer')

animals = [don, dog, mess,less]
for animal in animals:
    animal.make_sound()


