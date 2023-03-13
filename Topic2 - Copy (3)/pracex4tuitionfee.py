'''
TUITION FEE constants = 8000
increase is 2% p year for next 5 years

for n in range(years):
    increase = 0.02 * last year's tuition fee
    increased price = last year's tuition fee + 2% increase
    #increased price kept in running variable above
    #last year tuition fee - calculated using if else statement,
    #because no initial amount is set for starting year
    if n == 0:
        inc_price = 8000 + (0.02*8000)
        #initial amount needs to be on top of code
    #else statement then can do as above
    else:
        increase = 0.02 * last year's tuition fee
        increased price = last year's tuition fee + 2% increase
#print the tuition amount
    print(f'The fee for year' +str(n+1)+
    f' is {increased price}')
'''
TUITION_BASE= 8000
YEARS = 5

inc_price = 0
#loop for years
for n in range(YEARS):
    if n == 0:  #initial year
        inc_price = 8000 + (0.02*8000)
    else:  #rest of years
        increase = 0.02 * inc_price
        inc_price = inc_price + increase
    #increased price kept in running variable above
#print the tuition amount each iteration
    print(f'The fee for year' +str(n+1)+
    f' is {inc_price:.2f}')