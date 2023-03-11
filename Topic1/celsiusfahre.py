'''
F= 9/5C +32
F= ((9/5)*C) +32
get tempin Cel
calculate Fahrenheit
display F
'''

cels= float(input('enter temp in C: '))
fah= (9/5) * cels + 32
print('the temp in F is '+format(fah, '.1f'))

s1 = 'New York'
s2 = 'Boston'

if s1 > s2:
    print(s2)
    print(s1)
else:
    print(s1)
    print(s2)