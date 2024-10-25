numbers = [23,40,45,24,57,23,55,67]
odd = []
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odd.append(num)
print(odd)

players = ['sakib','musfiq','musta']
ages = [38,35,29]
age_comb =[]
for player in players:
    print('Player : ',player)
    for age in ages:
        print(player,age)
        age_comb.append([player,age])
print(age_comb)