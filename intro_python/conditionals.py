# in,not,not in,is,is not

a =  6
boss = True
if a > 1:
    print("5 er beshi")
elif a==2:
    print("2 er soman")
elif a <8:
    print("8 er theke choto")
else:
    print("akdom choto choto")

# if boss is True:
#     print("Tel er box niye astchi boss re tel dimu")
# else:
#     print("Luncher pore ashen")
if boss is not True:
    print("Luncher pore ashen")
else:
    print("tel niye astechi boss re tel dibo")

coin = "head"
#nested conditions
if boss == True:
    print("Boss your joss")
    if coin == "tail":
        print("tail hoyeche")
    else:
        print("head asheche")
else:
    print("Your loss not a boss")