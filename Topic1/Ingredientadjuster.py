'''
ingredients
sugar 1.5 c
butter 1 c
flour 2.75 c
this produces 48

48k = 1.5sc + 1bc + 2.75 fc
1k = s(1.5c/48)  + b(1c/48)   + f(2.75c/48)

get number of cookies
calculate cups for sugar . 1.5/48 X n
calculate cups for butter . 1/48 X n
calculate cups for flour . 2.75/48 X n
display number of each ingredient
display sugar
display butter
display flour
'''
#get number of cookies
cookies_desired= float(input('How many cookies to make? '))
#calculations
sugar= 1.5/48 * cookies_desired
butter= 1/48 * cookies_desired
flour= 2.75/48 * cookies_desired
#display
display= print('For '+format(cookies_desired, '.1f')+' cookies, \n'+
               'You will need \n'+
               format(sugar, '.2f')+ ' cups of sugar \n'+
               format(butter, '.2f')+ ' cups of butter \n'+
               format(flour, '.2f') + ' cups of flour ')