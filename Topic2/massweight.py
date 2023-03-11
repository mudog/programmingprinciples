'''
weight= mass X 9.8

enter mass
calculate weight
if weight > 500:
    print('It is too heavy')
elif weight < 100:
    print('It is too light')
'''
mass= int(input('Input the mass'))
weight = mass * 9.8
if weight > 500:
    print('It is too heavy')
elif weight < 100:
    print('It is too light')