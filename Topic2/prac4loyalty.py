'''
enter total sales
display points earned

0- 100 - 10 points
101 -500 - 20 points
>500 - 50 points

enter total sales
if total >= 0 and <=100:
    points = 10
elif total >= 101 and <=500:
    points = 20
elif total > 500:
    points = 50
else:
    print('This is not a valid number for total sales')

display points earned
'''
#enter total sales
total= int(input('Enter total sales in whole dollar: $'))

if total >= 0 and total <= 100:
    points = 10
elif total >= 101 and total <= 500:
    points = 20
elif total > 500:
    points = 50
else:
    print('This is not a valid number for total sales')

#display
display= print('You have earned '+str(points)+ ' loyalty points')