class Calculator:
    brand ='CASIO MS570'

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self,num1,num2):
        return num1 + num2
    def deduct(self,num1,num2):
        return num1 - num2
    def multipile(self,num1,num2):
        return num1 * num2
    def division(self,num1,num2):
        return num1 / num2

cal = Calculator(20,30)
print(cal.num1,cal.num2)