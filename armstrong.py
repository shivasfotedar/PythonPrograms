
def check_armstrong_number(number):
    length = len(number)
    number_to_be_checked = sum([ int(a)**length for a in number])
    return True  if int(number) == number_to_be_checked else False


number = input('Enter the number :')
if check_armstrong_number(number):
    print('{} is armstrong number'.format(number))
else:
    print('{} is not a armstrong number'.format(number))
