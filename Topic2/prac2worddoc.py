'''
typing speed= 30 w p min
two rates
    8hr or less= $21.75 p h
    else = $25 p h

enter number of words
display hours of labour required
display labour charges

enter number of words
calculate time taken to type number of words
    mins= numberw / speed 30 w p min
calculate time in hours =  mins/ 60
calculate charge
    if hours <= 8    21.75 * hours
    else   25 * hours
display time in hours
display charge
'''
#constants
TYPESPEED= 30
RATE_8HR= 21.75
RATE_OVER= 25
#get number of words
words = int(input('How many words do you require? '))
#time calcs
time_minutes= words / TYPESPEED
time_hours= time_minutes / 60
#charges
if time_hours <= 8:
    charges= RATE_8HR * time_hours
else:
    charges= RATE_OVER * time_hours

display=print('The hours of labour required is '+
              format(time_hours, '.1f')+
              '\nThe labour charges are: $'+
              format(charges, '.2f'))