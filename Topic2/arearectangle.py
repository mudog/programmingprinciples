'''
area = length x width

get length, width of rectangle 1
get length, width of rectanlge 2
calculate area rectanlge 1
calculate area rectangle 2

if area rec1 > area rec 2:
    print('area of rectangle 1 is greater than rectangle 2')
elif area rec1 < area rec 2:
    print('area of rectangle 2 is greater than rectangle 1')
else:
    print('the areas are the same')
'''
#using .split() method. does not work with int(), only input() and strings(?)
#string.split(separator,max)
length1,width1 = input('For rectangle1: Enter length followed by a space and then width').split()
length2,width2 = input('For rectangle2: Enter length followed by a space and then width').split()

#area of rectangles
area1 = int(length1) * int(width1)
area2 = int(length2) * int(width2)
print('area1= ',area1)
print('area2= ',area2)
#area1 bigger
if area1 > area2:
    print('area of rectangle 1 is greater than rectangle 2')
#area1 smaller
elif area1 < area2:
    print('area of rectangle 2 is greater than rectangle 1')
#same
else:
    print('the areas are the same')