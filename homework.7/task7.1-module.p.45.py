from math import pi

numberA = int(input('Enter number for A-side:' ))
numberB = int(input('Enter number for B-side:' ))

def area(numberA, numberB): 
    return (numberA * numberB) 

print ("Area = ", area(numberA, numberB)) 


r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

a = float(input('Enter first triange side: '))
b = float(input('Enter second triange side: '))
c = float(input('Enter third triangeside: '))

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
