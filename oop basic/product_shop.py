class Product:
    products = []
    def __init__(self, item, price, color):
        self.item = item
        self.price = price
        self.color = color

    def __repr__(self):
        return f'Shop Name: {self.name} {self.item} {self.price} {self.color}'



class Shop(Product):
    def __init__(self, name, item, price, color, quantity):
        self.quantity = quantity
        # self.products = []
        self.name = name
        super().__init__(item, price, color)

    def add_product(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.products.append(product)

    def buy_product(self, item, quantity):
        for product in self.products:
            if product['item'] == item and product['quantity'] >= quantity:
                print(f'Congratulations, you got the item {item}')
                return
        print('Sorry, we don\'t have this product or enough quantity')

    # def __repr__(self):
    #     return f'Shop Name: {self.name} {self.item} {self.price} {self.color} {self.quantity}'

shop = Shop('Gazi Bhai', 'TV', 14000, 'black', 4)
shop.add_product('Mobile', 90000, 2)
shop.add_product('Mouse', 400, 4)
print(shop)
shop.buy_product('Mobile', 2)
