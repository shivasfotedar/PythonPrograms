
def find_primes(number):
    for i in range(2,number+1):
        result = check_prime(i)
        print(result)
        if result:
            prime_numbers.append(i)

    return prime_numbers

def check_prime(number):
    prime = True
    if number <= 1:
        prime = False
    elif number == 2:
        prime = True
    else:
        for i in range(2,number//2+2):
            if number % i == 0:
                prime = False
                break

    return prime

number = int(input('Enter the number'))
prime_numbers = [] 
print(find_primes(number))