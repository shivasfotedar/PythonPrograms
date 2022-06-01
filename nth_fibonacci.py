def get_fibonacci(number):
    fibonacci_number = 0
    first = 0
    second = 1

    if number == 1:
        fibonacci_number = 0
    elif number == 2:
        fibonacci_number = 1
    else:
        for i in range(2,number):
            fibonacci_number = first + second
            first = second
            second = fibonacci_number
        
    return fibonacci_number

number = int(input('Enter the number :'))
print(get_fibonacci(number))