class Grandpa:
    def __init__(self) -> None:
        pass
    def propertiy(self):
        print('I have 5 corer taka')
    
class Father(Grandpa):
    def propertiy(self):
        print('I have 3 corer taka')
    
    def father_property(self):
        super().propertiy()

class Child(Father):
    def propertiy(self):
        print('I have 1 corer taka')
    def father_property(self):
        super().propertiy()
    def Grandpa_property(self):
        super().father_property()

ami = Child()
ami.propertiy()
ami.father_property()
ami.Grandpa_property()