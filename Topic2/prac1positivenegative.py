'''
get user input integer
if greater than 0:
    print positive
if less than 0:
    print negative
if 0:
    print zero

modulo2= input%2
if even - modulo2 >0
    print even
else
    print odd
'''

integer= int(input('Please input integer: '))
if integer > 0:
    print('Positive')
elif integer < 0:
    print('Negative')
else:
    print('Zero')

modulo2= integer%2
if modulo2 >0:
    print('Odd')
else:
    print('Even')