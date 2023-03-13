'''
use enter positive integer n
nested loop patter
*
**
***
rows and columns 2D

enter integer
for number in range(n):
    for number in range(n):
        print('*')
#
actually should be the inner loop referencing the iterating variable
needs two different variables to produce the pattern
2 dimensions 2 variables

for variable1 in range(n):
    for variable2 in range(n):
        print('*')

for row in range(n):
    for column in range(n+1):
        print('*')

#to change the way it prints
for row in range(n):
    for colmn in range(n+1): #+1 due to starting with 0 for colum
        print('*', end='')
    print()

'''

n= int(input('Enter integer n: '))
for n in range(n):
    for colmn in range(n+1):
        print('*', end='')
    print()
