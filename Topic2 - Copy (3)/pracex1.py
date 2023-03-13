'''
sum of series of positive numbers
sum of meaning running total
enter number one by one
negative number is sentinel to end

enter input in number variable
loop with condition to keep prompting until negative number is entered

display sum of all positive numbesr
'''
number= int(input('Enter positive numbers to add (to stop enter negative number): '))
#loop with condition to keep prompting until negative number is entered
#running total set to 0
total = 0
while number >= 0:
    total += number
    number= int(input('Enter positive numbers to add (to stop enter negative number): '))


#display
display = print(f'The sum is {total}')
print(str(total))