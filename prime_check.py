def check_prime(number):
    prime = True
    if number <=1:
        prime = False
    elif number == 2:
        prime = True
    else:
        for i in range(2,number//2+1):
            if number % i == 0:
                prime = False
                break
    
    return prime

number = int(input('Enter the number: '))

print(number,'is prime') if check_prime(number) else print(number, 'is not prime')