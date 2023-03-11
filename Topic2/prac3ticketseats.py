'''
class A cost $50
class B cost $30
class C cost $15

enter class ticket A, B or C
'''
CLASS_A= 50
CLASS_B= 30
CLASS_C= 15

class_check= input('Enter class of the ticket to purchase: ')
if class_check == 'A':
    print('The Class A ticket costs $'+str(CLASS_A))
elif class_check == 'B':
    print('The Class B ticket costs $'+str(CLASS_B))
elif class_check == 'C':
    print('The Class C ticket costs $' + str(CLASS_C))
else:
    print('This is not a valid ticket.')