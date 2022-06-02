
def get_max(numbers):
    max = numbers[0]
    for i in numbers:
        if max < i:
            max = i
    
    return max

numbers = [ a for a in input('Enter the array of numbers :').split()]
print('Max number', get_max(numbers))
