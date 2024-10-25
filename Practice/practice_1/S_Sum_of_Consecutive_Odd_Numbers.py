t = int(input())
while range(t):
    x, y = map(int, input().split())
    sum = 0
    if x <= y:
        for num in range(x+1, y):
            if num % 2 == 1:
                sum = sum + num
    else:
        for num in range(y+1,x):
            if num % 2 == 1:
                sum = sum + num
    print(sum)
 