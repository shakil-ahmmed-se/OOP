name = 'Sakib\'s khan' #escape
name2 = "sakib khan"
name3 ="""
    sakib khan
    number one
 """
print(name)

#string is a squence of characters.
for char in name2:
    print(char)
print(name2[3])
print(name2[1:6])
print(name2[::-1])
#mutable means changeable
#immutable means you can't change it
# name2[0] = 'R'
if 'khan' in name2:
    print('exsits')
print(name2.upper())