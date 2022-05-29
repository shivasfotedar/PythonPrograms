num = int(input('Enter the number :'))
factorial = 1
number = num
while num > 1:
    factorial *= num
    num -= 1

print('Factorial of {number} is {factorial}'.format(number = number,factorial = factorial))
