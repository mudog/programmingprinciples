'''
total amount of meal
charge for food
calculate tip 18%
calculate sales tax 7%
calculate total = charge + tip + sales tax
display each
'''
charge= float(input('how much were you charged for food? : $'))
tip= 0.18 * charge
sales_tax= 0.07 * charge
total= tip+sales_tax+charge

print('charged: $'+ format(charge,'.2f'), \
      'tip: $'+ format(tip,'.2f'), \
      'sales tax: $'+ format(sales_tax,'.2f'),\
      'Total: $'+ format(total,'.2f'))