def call():
    print('Call some one i dont know')
    return 'Call done'

class Phone:
    price = 1200
    color = 'blue'
    brand = 'Samsung'
    features = ['camera','speaker','hammer']

    def call(self):
        print('calling  on person')
    
    def send_sms(self,phone,sms):
        text = f'Sending SMS to :{phone} and message :{sms}'
        return text


my_phone = Phone()
print(my_phone.features)
my_phone.call()
sms = my_phone.send_sms(233932,'I wanna see you ')
print(sms)