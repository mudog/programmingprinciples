'''
get user height
display height

'''
height= int(input('Please enter your height in centimetres :'))
print('your height is '+ str(height) + ' cm')

'''
get favorite color
display favourite colour
'''
color= input('Please enter your favourite colour: ')
print(color)

'''
adds 2 to a and assigns the result to b
get/define a
assign result of addition to b

multiplies b times 4 and assigns result to a
'''
#gets input value, say 2
a= int(input('please enter value of a: '))
c= a +2
b= c
print('a= '+str(a)+' and b= '+str(b))  #if a=2, b prints 4

#code follows on using above results
c= b *4  #a=2 original, prints 16
a= c
#print(str(a,b))  does not work, takes a and b as int
print('a= '+str(a)+' and b= '+str(b)) #prints a=16, b=4

c= a /3.14
b= c
#print(str(a,b))
print('a= '+str(a)+' and b= '+str(b)) #prints a=16, b=5.xx

c= b - 8
a= c
#print(str(a,b))
print('a= '+str(a)+' and b= '+str(b)) #prints a=-2.xx, b=5.xx


'''
w,x,y,z are all integers
variable name result'''
w=5
x=4
y=8
z=2
result= x+y #12
print(str(result))
result= z*2 #4
print(str(result))
result= y/x #2  - actual 2.0
print(str(result))
result= y-z #6
print(str(result))
result= w//z #2
print(str(result))

'''
variable name total
assign sum of 10 and 14'''
total= 10+14
'''
variable name down_payment
get downpayment
variable name due
total- downpayment
'''
down_payment= float(input('please enter your down-payment: $'))
due= total-down_payment
print('You have due $:'+ format(due, '.2f'))
'''
variable name subtotal
variable total
subtotal *0.15
'''
subtotal= int(input('insert subtotal:'))
total= subtotal*0.15
print('Total: '+str(total))

'''
sales reference float value, 2 decp
'''
sales=5.1999
print(format(sales,'.2f'))

'''
format with comma s'''
number=1234567.456
print(format(number, ',.1f'))

'''
George@John@paul@ringo'''
