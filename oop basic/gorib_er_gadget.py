class Laptop:
    def __init__(self,brand, price, color, memory, ) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running Laptop {self.brand}'
    def coding(self):
        return f'Learning python and practicing'
    
class Phone:
    def __init__(self,brand, price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price 
        self.color = color
        self.dual_sim = dual_sim
    def run(self):
        return f'Phone tipa tipi'
    def phone_call(self,number,text):
        return f'Sending sms to {number} with : {text}'
    
class Camera:
    def __init__(self,brand, price, color, pixle) -> None:
        self.brand = brand 
        self.price = price
        self.color = color
        self.pixle = pixle

    def run(self):
        pass
    def change_lens(self):
        pass