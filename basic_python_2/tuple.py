def multiple():
    return 3,4
# print(multiple())

things = 'pen', 'tripod','water bottle','charger','phone','webcam','sunglass'
# print(type(things))
# print(things[0])
# print(things[-2])
# print(things[3:6])
if 'phone' in things:
    print('yes')
for item in things:
    print(item)
# things[0] = 'wagon'
# print(things)

print(len(things))

mega = ([2,3,4],[9,5,4,2,6])
# print(type(mega))
mega[0][1] =684
print(mega)