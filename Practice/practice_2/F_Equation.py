x,y = input().split()
x = int(x)
y = int(y)

sum = 0
for i in range(0,y+1,2):
    sum += x ** i

sum -= 1
print(sum)