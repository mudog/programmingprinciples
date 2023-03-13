'''
S = 1 + 1/2 + 1/4 + 1/8 +.... +1/2**n
S= 1/2**0 + 1/2**1 +/2**2 etc.
user enter positive integer n
if negative give error
definite loop  for steatement
for each iteration n increments by 1

n_value = int(input('Enter value n: '))
calculate sum of series
sum running total


display sum
'''
#user enter positive integer n
n_value = int(input('Enter value n: '))
if n_value < 0:
    print('Error n needs to be positive')

#definite loop  for steatement
#for each iteration n increments by 1
#running total totalsum set to 0
totalsum = 0
for number in range(n_value+1):
    totalsum += 1/ (2**number)

print(f'The total sum is {totalsum}')