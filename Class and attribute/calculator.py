class Calculator:
    brand = 'Casio MS570'

    def add(self,num1,num2):
        addition = num1 + num2
        return addition
    def substruct(self,num1,num2):
        sub = num1- num2
        return sub
    def multipile(self,num1,num2):
        multi = num1 * num2
        return multi
    def division(self,num1,num2):
        div = num1 / num2
        return div

    
cal = Calculator()
print(cal.brand)
print(cal.add(240,10))
print(cal.substruct(50,20))
print(int(cal.division(15,3)))

class Shop:
    shopping_mall = 'Jamuna'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


p1 = Shop('meh jabeeeen')
p1.add_to_cart('shoes')
p1.add_to_cart('phone')


nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)