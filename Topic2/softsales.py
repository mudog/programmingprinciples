'''
price - 99 per unit
calculate total
discount conditions
if 10-19  10%
if 20-49 20%
if 50-99 30%
if 100 or more 40%
else 0%
discount
calculate price after discount = total - discount

display
'''
UNIT_PRICE = 99
units = int(input('How many packages purchased? '))

total_price= UNIT_PRICE * units
discount_rate= 0

#conditions
if units >=10 and units <=19:
    discount_rate = 0.1
elif units >=20 and units <=49:
    discount_rate = 0.2
elif units >=50 and units <=99:
    discount_rate = 0.3
elif units >=100:
    discount_rate = 0.4
else:
    0.4

discount = discount_rate * total_price
balance = total_price - discount

print(f'Discount amount: ${discount:.2f}'+
      f'Balance: ${balance:.2f}')

