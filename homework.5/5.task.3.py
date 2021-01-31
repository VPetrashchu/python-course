n = int(input('Enter please, how many numbers you want fibonacci series = '))

if (n < 0):
    print('Negative sequences cannot be used in Fibonacci')

a = 0
b = 1
if n == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range (2, n):
        c = a + b
        a = b
        b = c
        print(c)
