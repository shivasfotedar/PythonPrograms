
amount = float(input('Enter the amount :'))
time = float(input('Enter the time in years :'))
rate = float(input('Enter the rate of interest PA :'))

compound_interest = amount*(((1 + rate/100)**time) - 1)
print('Compound interest is {:.2f}'.format(compound_interest))