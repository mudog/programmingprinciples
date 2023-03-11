'''
one acre = 43560 square feet
user to enter the total square feet and calculates number of acres
get square feet from user
calculate number of acre- divide by 43560
display acre
'''
square_feet= int(input('Enter total acres: '))
acre= square_feet /43560
print(str(square_feet)+' square ft equals to '+format(acre, '.2f')+' acres')