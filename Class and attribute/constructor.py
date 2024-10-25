class Phone:
    menufacture = 'China'

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self,phone,sms):
        text = f'sendin to {phone} this {sms}'
        return text
    
my_phone = Phone('Shakil','Techno',13000)
print(my_phone.owner,my_phone.brand,my_phone.price)
her_phone = Phone('Sinthi','Iphone',140000)
print(her_phone.owner,her_phone.brand,her_phone.price)

# my_phone.send_sms()
# her_phone.send_sms()

