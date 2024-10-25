#set:unnique items collection
numbers = [12,38,59,28,73,59,50,62,38]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
numbers_set.add(55)
print(numbers_set)

numbers_set.remove(62)
print(numbers_set)

for item in numbers_set:
    print(item)
if 9 in numbers_set:
    print('exsits')
elif 28 in numbers_set:
    print('28 is exits')

A ={1,3,5,7}
B ={1,2,3,4,5}
print(A & B)
print(A | B)