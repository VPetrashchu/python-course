list=[] 

print("Enter 4 numbers:")

for i in range(0, 4): 
    number = int(input())
    list.append(number)

print(list)

for i in list: 
    if i % 2 > 0:
        print("has odd")
        break
