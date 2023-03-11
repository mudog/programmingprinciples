'''
annual profit is 23 percent of total sales
user enter amount of total sales
display profit

get total sales
calculate sales profit 23%
display profit
'''
total_sales= float(input('Enter total sales: $ '))
profit= 0.23 * total_sales
print('Profit: $'+ format(profit,'.2f'))