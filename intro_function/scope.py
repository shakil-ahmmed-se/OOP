balance = 3000

def buy_thing(item,price):
    #local scope variable
    #you can acces global variable without using the global keyword
    dream_phone ='xphone'
    #if you want to access global variable ,you have to use global keyword
    global balance
    print(f'previous balance : ',balance)
    balance = balance-price
    print(f'balance after buying {item}: ',balance)

buy_thing('sunglass',1000)
print('global balance after buy: ',balance)