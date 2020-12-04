from functools import reduce

list_numbers = []
number = input ("Please, enter 4 numbers: ")
if (len(number) != 4): 
    print('Enter valid number')
else:
    # number = '12345678911234'
    list_of_numbers = list(number)

    total = 1
    for i in list_of_numbers:
        total *= int(i)

    print('Total is: ', total)

    list_of_numbers.reverse()
    print('Reverse number is: ', ''.join(list_of_numbers))
    list_of_numbers.sort()
    print('Sortede number is: ', ''.join(list_of_numbers))
