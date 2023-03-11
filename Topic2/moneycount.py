'''
enter number books
conditions
get points
display points
'''

books= int(input('Number of books purchased this month: '))

#conditions
points = 'invalid'
if books == 0:
    points = 0
elif books >=2 and books<4:
    points = 5
elif books >=4 and books<6:
    points = 15
elif books >=6 and books<8:
    points = 30
elif books >=8:
    points = 60

print(f'You have ernd ' +
      f'{points} points')