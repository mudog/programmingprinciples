'''Input temperature in Celsius (C)
calculates conversion to Fahrenheit (F)
formula
F = (9/5) C + 32
F = ((9/5) * C) + 32
Display to user
'''

def main():
    #input temp in Celsius
    celsius_temp= float(input('Please input the temperature in degrees Celsius: '))
    #calculate to Fahrenheint
    fahrenheit_temp= ((9/5) * celsius_temp) + 32
    #display one decimal point
    display_C= format(celsius_temp, '.1f')
    display_F= format(fahrenheit_temp, '.1f')
    #display to user
    display_user= print('The temperature is ' + display_C + ' degrees Celsius' + \
                        ' or ' + display_F + ' degrees Fahrenheit')

main()
