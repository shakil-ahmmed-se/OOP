#string(immutable)
a ='Hello'
for ch in a:
    print(ch,end="")
print()
#capitalize
b = 'phithron'
c ='PHITRHON'
print('capitalize : ',b.capitalize()) # capitalize :  Phithron
print('UpperCase : ',b.upper()) # UpperCase :  PHITHRON
print('LowerCase : ',b.lower()) # LowerCase :  phithronn
print('casefold : ',c.casefold()) # casefold :  phitrhon

#find
text = 'Hello, world'
src = 'd'
index = text.find(src)

if index != -1:
    print(f'The result {src} was found at index {index}')
else:
    print(f'Not found')

#count 
    
text ='Phiiiisssstttroon'
print(text.count('o'))

from collections import Counter
print(Counter(text))