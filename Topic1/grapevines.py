'''
V = (R- (2*E)) / S

get length of row in feet R
get amount of space by endpost assembly E
get amount of space between vines S
calculate V
display number of grapevines that will fit in the row
'''
row_length= float(input('How long is the row (ft)? '))
endpost= float(input('How long is one endpost assembly (ft)? '))
space= float(input('How long is a space between vines (ft)? '))

vines= (row_length- (2*endpost)) // space
display= print('You can fit '+str(vines)+ ' vines in a row.')