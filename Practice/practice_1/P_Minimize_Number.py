t = int(input())
a = list(map(int, input().split()))
opt = 0
even = True

for num in a:
    if num % 2 != 0:
        even = False
        break

if even:
    while all(num % 2 == 0 for num in a):
        a = [num // 2 for num in a]
        opt += 1

print(opt)
