variable1 = 35
variable2 = 40

print('Value before changing:\n 1st variable - ', variable1, '\n', '2nd variable - ', variable2)
variable1, variable2 = variable2, variable1
print('Value after changing:\n 1st variable - ', variable1, '\n', '2nd variable - ', variable2)