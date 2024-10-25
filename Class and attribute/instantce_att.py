class Shop:
    shopping_mall = 'Jamuna'

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute

    def add_to_cart(self,items):
        self.cart.append(items)
    
mehu = Shop('mehu jabin')
mehu.add_to_cart('saree')
mehu.add_to_cart('bag')
print(mehu.cart)

nisho = Shop('nishu')
nisho.add_to_cart('watch')
nisho.add_to_cart('hat')
print(nisho.cart)

apurbo = Shop('age purbo chilo')
apurbo.add_to_cart('pant')
print(apurbo.cart)