class shop:
    cart = [] # cart is a class attribute

    def __init__(self,buyer):
        self.buyer = buyer
    def add_to_cart(self,items):
        self.cart.append(items)
    
mehu = shop('mehu jabin')
mehu.add_to_cart('lehenga')
mehu.add_to_cart('bag')
print(mehu.cart)

nisho = shop('nisho')
nisho.add_to_cart('watch')
nisho.add_to_cart('shirt')
print(nisho.cart)