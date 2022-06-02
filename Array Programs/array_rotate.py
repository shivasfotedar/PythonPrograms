def get_rotated_array(numbers, rotate):
    rotated_list = []
    start = rotate
    index = 0

    while start < len(numbers):
        rotated_list.append(numbers[start])
        start+=1
        index+=1
    
    if start == len(numbers):
        start = 0
        while start < rotate:
            rotated_list.append(numbers[start])
            start+=1
    
    return rotated_list




numbers = [int(a) for a in input('Enter the numbers :').split()]
rotate = int(input('Enter the rotation count :'))
print('Rotated List', get_rotated_array(numbers,rotate))