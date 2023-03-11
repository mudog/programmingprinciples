'''
primary colors- red, blue, yellow
secondary colors - red + blue = purple
- red + yellow = orange
- blue + yellow= green

enter primary_colour1
enter primary_colour2
if primary_colour1 != "red" or "blue" or "yellow":
    print('Error: colour1 is not a valid primary colour')
if primary_colour2 != "red" or "blue" or "yellow":
    print('Error: colour2 is not a valid primary colour')

secondary= 0
if primary_colour1 == "red" and primary_colour2 =="blue" OR \
primary_colour1 == "blue" and primary_colour2 =="red":
    secondary= "purple"
elif primary_colour1 =="red" and primary_colour2 =="yellow" OR \
colour1 =="yellow" and primary_colour2 =="red":
    secondary= "orange"
elif primary_colour1 =="blue" and primary_colour2 =="yellow" OR \
primary_colour1 =="yellow" and primary_colour2 =="blue":
    secondary= "blue"


print('By mixing ' + primary_colour1 +
            ' and '+ primary_colour2 +', the secondary colour is '+
            secondary_colour)

'''
#enter primary
primary_colour1= input('Enter primary colour 1: ')
primary_colour2= input('Enter primary colour 2: ')

#error message if not primary
if primary_colour1 != "red" or "blue" or "yellow":
    print('Error: colour1 is not a valid primary colour')
if primary_colour2 != "red" or "blue" or "yellow":
    print('Error: colour2 is not a valid primary colour')

#process secondary colour
secondary= 0
if (primary_colour1 == "red" and primary_colour2 =="blue") or  \
        (primary_colour1 == "blue" and primary_colour2 =="red"):
    secondary= "purple"
elif (primary_colour1 =="red" and primary_colour2 =="yellow") or \
(primary_colour1 =="yellow" and primary_colour2 =="red"):
    secondary= "orange"
elif (primary_colour1 =="blue" and primary_colour2 =="yellow") or \
        (primary_colour1 =="yellow" and primary_colour2 =="blue"):
    secondary= "blue"

#display
print('By mixing ' + primary_colour1 +
            ' and '+ primary_colour2 +', the secondary colour is '+
            secondary)