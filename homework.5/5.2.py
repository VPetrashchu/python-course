for i in range(1,101,2):
    print("100 has odd's number: ", i)

number = 101
while (number > 0):
    number -= 1
    if number % 2 == 0:
        continue
    
    print("100 has odd's number,: ", number)