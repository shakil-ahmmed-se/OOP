

t = int(input())
a = list(map(int,input().split()))
count = {}
remove = 0
for num in a:
    # print(num)
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
        
for key, val in count.items():
    # print(count,num)
    if key > val:
        remove +=  val
    elif key < val:
        remove += val - key
    
print(remove)
