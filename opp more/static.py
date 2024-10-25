class Shopping:
    cart = [] # class or static attribute
    origin = 'China'
    def __init__(self,name, location) -> None:
        self.name = name 
        self.location = location
    
    def purchase(self,item, price, amount):
        remaining = amount - price
        print(f'Buygin {item} for {price} and remaining {remaining}')

    @staticmethod
    def multiply(a, b):
        reust = a * b
        print(f'Multiplication : {reust}')

    @classmethod
    def hudai_dekhi(self,item):
        print('Hudai dekhi kinmu na',item)

basundhara = Shopping('Bashun', 'Not popular location')
# basundhara.purchase('lungi',500,1200)
basundhara.hudai_dekhi('lungi') #class methond

# Shopping.purchase(2,3 , 4)
Shopping.hudai_dekhi('pant') # static method
Shopping.multiply(4 , 6)