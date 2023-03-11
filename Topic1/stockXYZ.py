'''XYZ purchased
units 500
rate $25.04
commission 2.3% of total purchase price

XYZ sold the stock
units 500
rate $36.06
comm 2.1% of total selling price

software reqs
-money paid for the stock
-commision to broker for buying
-money got for selling
-commission to broker for selling
-net profit

'''

'''
def main():
    #get units purchase
    buy_quantity= int(input('Enter number of shares bought '))
    #get per share price purchased
    buy_rate= float(input('and now enter the price per unit: $ '))
    #calculate total purchase
    buy_total = buy_quantity * buy_rate
    #calculate commission for buy
    buy_commision= 0.023 * buy_total

    #
'''
def main():
    #calculate total purchase
    buy_total= 500 * 25.04
    buy_comm= 0.023 * buy_total
    #calculate total sale
    sell_total= 500 * 36.06
    sell_comm= 0.021 * sell_total
    #calculate net profit
    net= sell_total - buy_total - buy_comm - sell_comm
    #display to user
    display= print('XYZ has paid $ '+ format(buy_total, '.2f') +' to buy the stock' \
                   + ' and has paid the broker $ ' + format(buy_comm, '.2f') + ' for the purchase'\
                   + '\nXYZ has sold the stock for $ ' + format(sell_total,'.2f')  \
                   + ' and paid the broker $ ' + format(sell_comm, '.2f')  \
                   +'for the sale' + \
                   '\nThe net profit XYZ has made is $ ' + format(net,'.2f'))


main()
