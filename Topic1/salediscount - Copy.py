def main():
  discount=0.2


  sale_price= float(input('Please enter the \
price of item you wish to purchase')) * (1.0 - discount)
                            

  checkout= format(sale_price,'.2f')
                            


  loyalty_points= int(10* sale_price)
                            
  print('The total price is '+ checkout+ '.'+ 'You have earned '+ str(loyalty_points) + ' loyalty points with this purchase.')


main()

