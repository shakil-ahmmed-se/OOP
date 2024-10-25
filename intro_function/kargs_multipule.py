def full_name(first,last):
    name = f'Full name is: {first} {last}'
    return name
#take peratmeter in order(serial wise)
# Name = full_name('Allu','Kodu')
Name = full_name(last='Kodu',first='Alu')
print(Name)

def famous_name(first,last,**addition):
    name = f'{first} {last}'
    # print(addition['title'])
    for key,value in addition.items():
        print(key,value)
    return name
name = famous_name(first='taher',last='Ali',title='Hujur',title2='shoyekh',last2 = 'taherri')
print(name)

#def function_name(num1,num2,*args,*kargs):
#return multipule thing from any array
def a_lot(num1,num2):
    sum = num1 + num2
    multi = num1 * num2
    remain = num1 - num2
    # return [sum,multi,remain]
    return sum,multi,remain
everything = a_lot(55,21)
print(everything)