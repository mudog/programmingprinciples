'''
6/10/60
month x day = year
this is magic date

enter day
enter month
enter year
calculate magicdm = month x day
if magicdm == year:
    print('This is a magic date')
else:
    print('This date is not magic.')
'''
day, month, year =  input('Enter a date in following format'+
                              'day/month/last two digits of year: ').split('/')
magicdm= int(month) * int(day)
if magicdm == int(year):
    print('This is a magic date')
    print(str(magicdm))
else:
    print('This date is not magic.')
    print(str(magicdm))