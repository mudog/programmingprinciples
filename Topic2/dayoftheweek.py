'''
get number range 1 through 7
1 Monday
2 Tuesday
display error message if outside range


'''
#get number
numberget= int(input('Please enter a number '))

#check within range
if numberget >= 1 and numberget <=7:
    #monday
    if numberget == 1:
        print('Monday')
    elif numberget == 2:
        print('Tuesday')
    elif numberget == 3:
        print('Wednesday')
    elif numberget == 4:
        print('Thursday')
    elif numberget == 5:
        print('Friday')
    elif numberget == 6:
        print('Saturday')
    elif numberget == 7:
        print('Sunday')
else:
    print('Error')