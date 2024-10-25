#lambda
# def double(x):
#     return x*2
double = lambda num : num * 2
square = lambda num : num * num
result = double(44)
result2 = square(5)
# print(result)
# print(result2)

add = lambda x,y : x+y
sum = add(4,5)
# print(sum)

numbers = [12,38,59,28,73,59,50,62,38]
# double_num = map(double,numbers)
double_num = map(lambda x:x*2,numbers)
print(numbers)
print(list(double_num))

actors = [
    {'name':'sabana', 'age' :65},
    {'name':'sabnur', 'age' :45},
    {'name':'sabila norr', 'age' :30},
    {'name':'srabonti', 'age' :38},
    {'name':'sahon', 'age' :48},
]

juniors = filter(lambda actor : actor['age'] <40,actors)
fivers = filter(lambda actor : actor['age'] % 5 == 0,actors)

# print(list(juniors))
# print(list(fivers))
try:
    result =20//5
except:
    print("error happened")
finally:
    print("finally here")