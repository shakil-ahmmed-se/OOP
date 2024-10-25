class shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item' : item,'price': price,'quantity': quantity}
        self.cart.append(product)

    def remove_item(self,item):
        for i in self.cart:
            # print(i['item'])
            if i['item'] == item:
               del self.cart['item']
           

            

    def checkOut(self,amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('Total price',total)
        if total > amount:
            print(f'Plese provide {total -amount} more')
        else:
            change = amount - total
            print(f'Take your change {change} taka')
nisho = shopping('Nisho')
nisho.add_to_cart('watch',800,2)
nisho.add_to_cart('dim',12,5)
print(nisho.cart)
nisho.checkOut(1000)
nisho.remove_item('dim')
print(nisho.cart)