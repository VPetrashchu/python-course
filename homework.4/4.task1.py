number = int(input('Enter number: '))
fact = 1
for i in range(1, number + 1):
    fact = fact * i

print('Factorial is: {}'.format(fact))

# while ( number > 0):
#     fact = fact * number
#     number = number - 1
# print('Factorial is: {}'.format(fact))
