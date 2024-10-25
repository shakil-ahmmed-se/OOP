from abc import ABC,abstractmethod

class Resturant:
    def __init__(self,resturant_name) -> None:
        self.resturant_name = resturant_name
        self.products =[]
        self.workers =[]
        
    def add_product(self,products_name,quantity):
        product = (products_name,quantity)
        self.products.append(product)