'''one pound = 0.454 kg
Input mass of object in pounds
Calculate object in kilogram
display mass of object in kilogram
'''

def main():
    #get mass of object
    mass_pounds= float(input('Please enter the mass of the objectin pounds: '))
    #calculate to kg
    mass_kg= mass_pounds * 0.454
    #format pounds to width 10 and decimal places 2
    display_pounds= format(mass_pounds, '10,.2f')
    #format kilogram to width 10 and decimal places 2
    display_kg= format(mass_kg, '10,.2f')
    #display back 
    display_user= print('The mass in pounds is '+ display_pounds + 'lbs' +
                      '\nThe converted mass to kilogram is ' + display_kg + ' kg.')
    
main()
