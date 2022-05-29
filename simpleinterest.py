amount = float(input('Enter the amount :'))
time = float(input('Enter the time in years :'))
rate = float(input('Enter the rate of interest per annum :'))

simple_interest = (amount * rate * time)/100
print('Simple Interest :'.format(simple_interest))