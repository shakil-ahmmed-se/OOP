class Person:
    def __init__(self,name, age, height, weight) -> None:
        self.name = name 
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangso polaw')

    def exercise(self):
        raise NotImplementedError

class Crickter(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team

        super().__init__(name, age, height, weight)
    #over ride
    def eat(self):
        print('vegitables')
    def exercise(self):
        print('gym na giye regular excersie koro')
    # plus sing operator overload
    def __add__(self,other):
        return self.age + other.age
    # mutlipule sing operator overload
    def __mul__(self,other):
        return self.weight * other.weight
    # greater than sing operator overload
    def __gt__(self,other):
        return self.age > other.age
    

sakib = Crickter('sakib',38,68,70,'BD')
mushi = Crickter('Musi',36,65,69,'Bd')

# sakib.eat()
# sakib.exercise()

# plus sign overload
print(45 + 63)
print('sakib' + 'rakib')
print([12,39,49] + [1,2,4,5])

print(sakib + mushi)
print(sakib * mushi)
print(sakib > mushi)