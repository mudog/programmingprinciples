'''
compound interest formula
A= P * (    (1 + (r/n)
                        )** (n*t) )

input amount of principal originally deposited P
input annual interest rate % r
input number of times per year interest is compounded ,\
suggest 12 monthly, 4 quarterly, n
input number of years account will be left to earn interest t
calculate compound interest
display amount of money in the account A
'''
#inputs
principal_depo= float(input('How much was the principal'+
                            'in the original deposit? $'))
rate_annual= float(input('Insert annual interest rate in %'))
number_compound= float(input('How many times is the interest '+
                             'compounded in a year? '+
                             'e.g. 12 if monthly, 4 if quarterly '))
time_interest= float(input('How many years will the account'+
                           ' earn interest for? '))

#calculate money in account
account= principal_depo * (    (1 + (rate_annual/number_compound)
                        )** (number_compound*time_interest) )

#display
print('The account will have $'+format(account,'.2f')+
      ' after '+format(time_interest, '.0f') + ' years.'
      )