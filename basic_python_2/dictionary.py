numbers = [12, 38, 59, 28, 73, 59, 50, 62, 38]
person1 = ['kala chan', 'kalipur', 25, 'student']
#key value pair
#dictionary
#object
# hash table
# overlap with set
person = {'name':'kala pakhi', 'address':'kaliapur', 'age':23, 'job':'facebooker'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name'] ='sada pakhi'
del person['age']
print(person)

#dictionary looping
for key,value in person.items():
    print(key,value)