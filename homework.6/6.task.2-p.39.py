# for i in range(2,11,2):
#     print("Numbers that are divisible by 2: ", i)

# for i in range(3,11,3):
#     print("Numbers that are divisible by 3: ", i)
n = 10

list2 = []
list3 = []
list23 = []
while (n > 0):
    if n % 2 == 0:
        list2.append(n)
    elif n % 3 == 0:
        list3.append(n)
    else:
        list23.append(n)
    n -= 1 

print("Numbers that are divisible by 2: ", list2)
print("Numbers that are divisible by 3: ", list3)
print("Numbers that are not divisible by 2 and 3: ", list23)

