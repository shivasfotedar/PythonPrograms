def is_fibonacci(number):
    fibonacci_number = 0
    first = 0
    second = 1
    for i in range(number):
        fibonacci_number = first + second
        first = second
        second = fibonacci_number
        if fibonacci_number == number:
            return True     
        elif fibonacci_number > number:
            return False
            break

number = int(input('Enter the number :'))
print(number, 'is fibonacci number') if is_fibonacci(number) else print(number,'is not fibonacci number')
