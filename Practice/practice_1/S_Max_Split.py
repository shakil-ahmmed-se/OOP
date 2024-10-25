input_string = input().strip()
n = len(input_string)
cnt_L = 0
cnt_R = 0
result = []
for ch in input_string:
    if ch == 'L':
        cnt_L += 1
    else:
        cnt_R += 1
    # print(cnt_L,cnt_R)
    if cnt_R == cnt_L:
        result.append(input_string[:cnt_R+cnt_L])
        input_string = input_string[cnt_L+cnt_R:]
        cnt_L = 0
        cnt_R = 0
print(len(result))
for substring in result:
    print(substring)
