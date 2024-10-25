simpleDictionary = {
    'class' :{
        'student':{
            'name':'Mike',
            'marks' :{
                'physics':70,
                'history':80
            }
        }
    }
}
# print(simpleDictionary['class']['student']['marks']['history'])


# lst = list(map(int,input().split()))

lst = [1,2,3,4]

# for i in range(0, len(lst)):
#     lst[i] = lst[i] * lst[i]
# print(lst)

# def sq(i):
#     return i*i
# result = map(sq,lst)
# print(list(result))

result = map(lambda i:i*i,lst)
print(list(result))