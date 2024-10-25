class Shop:
    def __init__(self, shop_name) -> None:
        self.shop_name = shop_name
        self.products = []
        self.sellers = []
        self.customers = []
        self.order = []

 

    def create_seller_account(self, email,password):
        seller = Seller(email, password)
        self.sellers.append(seller)

    def create_customer_account(self, email, password):
        customer =Customer(email, password)
        self.customers.append(customer)

    def add_product(self, product_name, price, quantity):
        product = Product(product_name, price, quantity)
        self.products.append(product)
        # print(f'{product_name} added successfully')

    def order(self, name,quantity):
        for product in self.products:
            if product.name == name and product.quantity >= quantity:
                product.quantity -= quantity
                self.order.append(name,quantity)
                print(f'{product.name} order successfully')

    def show_product(self):
        for product in self.products:
            print(f'{product.name} : price: {product.price} quantity: {product.quantity}')

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Users:
    def __init__(self, email, password):
      
        self.email = email
        self.password = password


class Customer(Users):
    def __init__(self, email, password):
        self.wallet = 0
        super().__init__(email, password)
    def order(self,shop,product_name,quantity):
        shop.order(product_name,quantity)

    def show_product(self, shop):
        shop.show_product()


class Seller(Users):
    def __init__(self, email, password):
        super().__init__(email, password)

    def add_product(self, shop_name, product_name, price, quantity):
        shop_name.add_product(product_name, price, quantity)

    def show_product(self, shop):
        shop.show_product()




amar_shop = Shop('amar_shop') 
# amar_shop.add_product()
broker = Seller('musi@gmail.com','2131')
broker.add_product(amar_shop,'apple',120,10)
broker.add_product(amar_shop,'orange',200,30)
broker.add_product(amar_shop,'Gouva',80,20)
# broker.show_product(amar_shop)
ami = Customer( 'sakib@gmail.com', '1231')
ami.show_product(amar_shop)
ami.order(amar_shop,'apple',8)
