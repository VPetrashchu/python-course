list=[] 

print("Enter 4 numbers:")

for i in range(0, 4): 
    number = int(input())
    list.append(number)

print('Maximum value: ', max(list))
print('Minimum value: ', min(list))