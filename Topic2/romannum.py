'''
enter number within 1 through 10
display corresponding roman numeral
if outside display error
'''
number= int(input('Enter a number within range 1 through 10 '))

if number >=1 and number <=10:
    if number ==1:
        print('I')
    elif number ==2:
        print('II')
    elif number == 3:
        print('III')
    elif number == 4:
        print('IV')
    elif number == 5:
        print('V')
    elif number == 6:
        print('VI')
    elif number == 7:
        print('VII')
    elif number == 8:
        print('VIII')
    elif number == 9:
        print('IX')
    elif number == X:
        print('X')
else:
    print('Error')