'''
enter A
enter B
enter C

find middle number
if (A >= B and A<= C) or (A >= C and A<= B):
    A is middle number
if (B >= A and B<= C) or (B >= C and B<= A):
    A is middle number
if (C >= A and C<= B) or (C >= B and C<= A):
    C is middle number

'''
a= int(input('Enter integer for a: '))
b= int(input('Enter integer for b: '))
c= int(input('Enter integer for c: '))

if (a >= b and a<= c) or (a >= c and a<= b):
    print('A is middle number')
if (b >= a and b<= c) or (b >= c and b<= a):
    print('B is middle number')
if (c >= a and c<= b) or (c >= b and c<= a):
    print('C is middle number')