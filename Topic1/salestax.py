'''
user enter amount purchase
calculate state tax 5%
calculate county salestax 2.5%
display - purchase
- state sales
-county sales
total sales tax
total sales= purchase + total sales tax

'''
purchase=float(input('Enter amount of purchase: $ '))
st_tax= 0.05 * purchase
cs_tax= 0.025 * purchase
total_tax= st_tax + cs_tax
totalsales= total_tax+ purchase

print('Amount of purchase: $'+format(purchase, ',.2f'), \
      'amount of state tax: $'+format(st_tax, ',.2f'), \
      'amount of county state tax: $'+format(cs_tax,',.2f'),\
      'amount of total tax: $'+format(total_tax, ',.2f'),\
    'Total sales: $'+format(totalsales,',.2f'), sep='\n')