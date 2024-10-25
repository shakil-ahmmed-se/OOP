numbers = [45,56,12,89,87,32,86,59,46]
print(numbers[-4],numbers[4])

#list(start : end)
print(numbers[2:6])
print(numbers[1:7])

#list(start : end : step)
print(numbers[1:8:2])
#ulta dike print
print(numbers[7:2:-1])
print(numbers[3:])
print(numbers[:6])
print(numbers[:])
print(numbers[::-1])


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana',4)) #find the next banana starting at position 4
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)