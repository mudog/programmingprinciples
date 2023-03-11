Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Trevis')
Trevis
print("Python's the best!")
Python's the best!
print('The cat said "meow."')
The cat said "meow."

discount=0.2
sale price= float( input('Please enter the price of \item you wish to purchase'))* discount
SyntaxError: invalid syntax

sale_price= float(input('Please enter the \
price of item you wish to purchase')) * discount
Please enter the price of item you wish to purchase
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sale_price= float(input('Please enter the \
ValueError: could not convert string to float: ''
sale_price= float(input('Please enter the \
price of item you wish to purchase')) * discount
                            
Please enter the price of item you wish to purchase1
print (sale_price, .2f)
                            
SyntaxError: invalid decimal literal
print(sale_price, .2f)
                            
SyntaxError: invalid decimal literal
print(sale_price,'.2f')
                            
0.2 .2f
sale_price= float(input('Please enter the \
price of item you wish to purchase')) * (1.0 - discount)
                            
Please enter the price of item you wish to purchase100
print(sale_price,'.2f')
                            
80.0 .2f
sale_price= float(input('Please enter the \
price of item you wish to purchase')) * (1.0 - discount)
                            
Please enter the price of item you wish to purchase100
checkout= format(sale_price,'.2f')
                            
print(checkout)
                            
80.00
print('The total price is '+ checkout+ '.'\+ 'You have earned '+ (10*checkout)+ 'loyalty points with this purchase.')
                            
SyntaxError: unexpected character after line continuation character
print('The total price is '+ checkout+ '.'+ 'You have earned '+ (10*checkout)+ 'loyalty points with this purchase.')
                            
The total price is 80.00.You have earned 80.0080.0080.0080.0080.0080.0080.0080.0080.0080.00loyalty points with this purchase.
print('The total price is '+ checkout+ '.'\+ 'You have earned '+ (10*int(checkout))+ 'loyalty points with this purchase.')
                            
SyntaxError: unexpected character after line continuation character
print('The total price is '+ checkout+ '.' \ + 'You have earned '+ (10*int(checkout))+ 'loyalty points with this purchase.')
                            
SyntaxError: unexpected character after line continuation character
print('The total price is '+ checkout+ '.' + 'You have earned '+ (10*int(checkout))+ 'loyalty points with this purchase.')
                            
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print('The total price is '+ checkout+ '.' + 'You have earned '+ (10*int(checkout))+ 'loyalty points with this purchase.')
ValueError: invalid literal for int() with base 10: '80.00'
print('The total price is '+ checkout+ '.'\+ 'You have earned '+ (10*int(sale_price))+ 'loyalty points with this purchase.')
                            
SyntaxError: unexpected character after line continuation character
print('The total price is '+ checkout+ '.'+ 'You have earned '+ (10*int(sale_price))+ 'loyalty points with this purchase.')
                            
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print('The total price is '+ checkout+ '.'+ 'You have earned '+ (10*int(sale_price))+ 'loyalty points with this purchase.')
TypeError: can only concatenate str (not "int") to str
print('The total price is '+ checkout+ '.'+ 'You have earned '+ (10*int(sale_price))+ 'loyalty points with this purchase.')
                            
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print('The total price is '+ checkout+ '.'+ 'You have earned '+ (10*int(sale_price))+ 'loyalty points with this purchase.')
TypeError: can only concatenate str (not "int") to str
print('The total price is '+ checkout+ '.'+ 'You have earned '+ (10*sale_price)+ 'loyalty points with this purchase.')
                            
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print('The total price is '+ checkout+ '.'+ 'You have earned '+ (10*sale_price)+ 'loyalty points with this purchase.')
TypeError: can only concatenate str (not "float") to str
print('The total price is '+ checkout+ '.'+ 'You have earned '+ str(10*int(sale_price))+ 'loyalty points with this purchase.')
                            
The total price is 80.00.You have earned 800loyalty points with this purchase.
loyalty_points= 10 * sale_price
                            
print('The total price is '+ checkout+ '.'+ 'You have earned '+ str(loyalty_points) + 'loyalty points with this purchase.')
                            
The total price is 80.00.You have earned 800.0loyalty points with this purchase.
The total price is 80.00.You have earned 800.0loyalty points with this purchase.
                            
SyntaxError: invalid decimal literal

loyalty_points= int(10* sale_price)
                            
print('The total price is '+ checkout+ '.'+ 'You have earned '+ str(loyalty_points) + 'loyalty points with this purchase.')
                            
The total price is 80.00.You have earned 800loyalty points with this purchase.
print('The total price is '+ checkout+ '.'+ 'You have earned '+ str(loyalty_points) + ' loyalty points with this purchase.')
                            
The total price is 80.00.You have earned 800 loyalty points with this purchase.
