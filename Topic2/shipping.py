'''
enter weight
if 2 p or less $1.50 p round
if weight >2 and weight<=6 $3.00
if weight >6 and weight<=10 $4.00
if weight >10 $4.75

display charges
'''
weight= float(input('What is weight in pounds? '))

#conditions
charges= 'invalid'

if weight <= 2:
    charges = 1.5
elif weight >2 and weight <=6:
    charges = 3
elif weight >6 and weight <=10:
    charges = 4
elif weight >10:
    charges = 4.75

print(f'For weight of {weight} pounds \n' +
      f'Charge: ${charges:.2f} per round')