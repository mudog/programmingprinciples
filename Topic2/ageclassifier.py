'''
enter age

display whether infant, child , teenager, adult

enter age
if age <=1:
    print('Infant')
elif age >1 and age<13:
    print('Child')
elif age >=13 and age<20:
    print('Teenager')
elif age > 20:
    print('Adult')
'''
age= int(input('Enter age: '))

if age <=1:
    print('Infant')
elif age >1 and age<13:
    print('Child')
elif age >=13 and age<20:
    print('Teenager')
elif age > 20:
    print('Adult')