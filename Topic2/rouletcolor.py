'''
roulette - 0 to 36
0 - green
1-10 red for odd
1-10 black for even
11-18 black for odd
11-18 red for even
19-28 red for odd
19-28 black for even
29036 black for odd
29-36 red for even

enter pocket number
conditions for 0
conditions for range 1-10
conditions for range 11-18
conditions for range 19-28
conditions for range 29-36

dislay colour
'''
pocket= int(input('enter pocket no.: '))

#condition 0
colour= 'No number picked'
if pocket == 0:
    colour= 'green'

#condition range 1-10
elif pocket >= 1 and pocket <=10:
    if pocket % 2 == 0:
        colour = 'red'
    else:
        colour = 'black'

#condition range 11-18
elif pocket >= 11 and pocket <=18:
    if pocket % 2 == 0:
        colour = 'black'
    else:
        colour = 'red'

#condition range 19-28
elif pocket >= 19 and pocket <=28:
    if pocket % 2 == 0:
        colour = 'red'
    else:
        colour = 'black'
#condition range 29-36
elif pocket >= 29 and pocket <=36:
    if pocket % 2 == 0:
        colour = 'black'
    else:
        colour = 'red'

else:
    colour = 'Error'

#display
print('Colour: '+colour)