"""
purchased stock
number = 2000
price = $40 p share
paidcommision= 3% price

sold stock
number = 2000
saleprice= $42.75 p share
paidcomsale= 3% saleprice

Display price
display paidcomision
display saleprice
display paidcomsale
display money left at the end
"""
#constants
SHARE_PURCHASE= 2000
TOTAL_PURCHASE= SHARE_PURCHASE * 40

COMM_PURCHASE= 0.03 * TOTAL_PURCHASE

SHARE_SALE= 2000
TOTAL_SALE= SHARE_SALE * 42.75

COMM_SALE= 0.03 * TOTAL_SALE

#money left
net_sale= TOTAL_SALE - (TOTAL_PURCHASE +
                        COMM_SALE + COMM_PURCHASE)
#display
display= print('Total purchase: $'+format(TOTAL_PURCHASE, '.2f') +
               '\nCommission paid on purchase: $'+
               format(COMM_PURCHASE, '.2f')+
               '\n\nTotal sale: $'+
               format(TOTAL_SALE, '.2f')+
               '\nCommission paid on sale: $'+
               format(COMM_SALE, '.2f')+
               '\n\nThe net sale is $'+
               format(net_sale, '.2f')
               )
if net_sale >=0:
    print('You have made a profit!')
else:
    print('You have made a loss.')
