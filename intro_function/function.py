def double_it(num):
    result = num * 2
    print('inside the function : ',result)
    return result


double_it(88)

def sum(num1,num2):
    result = num1 + num2
    return result
total = sum(44,39)
print(total)
final = double_it(total)
print(final)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")