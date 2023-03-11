'''
purchasing five items
ask for price of item
displays subtotal of the sale
amount of sales tax, 7 percent
and Total

get item 1
get item 2
get item 3
get item 4
get item 5
calculate subtotal 1+2+3+4+5
calculate sales tax amount = sales tax X subtotal
calculate total=  sales tax amount + subtotal
'''
i_1= float(input('please enter value of item1: '))
i_2= float(input('please enter value of item2: '))
i_3= float(input('please enter value of item3: '))
i_4= float(input('please enter value of item4: '))
i_5= float(input('please enter value of item5: '))

subtotal= i_5+ i_4 +i_3 +i_2 +i_1
print('Your subtotal is: $'+format(subtotal, ',.2f'))
s_tax= subtotal * 0.07
print('Your amount of sales tax is: $'+format(s_tax, ',.2f'))

total= format(subtotal + s_tax, ',.2f')
print('Your total is: $'+total)