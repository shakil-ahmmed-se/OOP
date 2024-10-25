t = int(input())
a = list(map(int,input().split()))
min_num =min(a)
mx_num = max(a)

mx_index = a.index(mx_num)
min_index = a.index(min_num)
a[mx_index],a[min_index] = a[min_index],a[mx_index]
print(*a)