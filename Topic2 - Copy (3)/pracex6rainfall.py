'''
enter number of years

outer loop
for n_years in range(years):
    inner loop
    for n_months in range(12):
        print(f'Input rainfall for '+
            f'Month {n_months} ', end='')
        rainfall_month= float(input(' in millimeters: '))
#getting all monthly rainfall, need to add them up together
#need running variable - total , put at start of code set to 0
total_rainfall =0
#getting all months, need to add number of months too
total_months = 0
innerloop
for n_months in range(12):
        print(f'Input rainfall for '+
            f'Month {n_months} ', end='')
        rainfall_month= float(input(' in millimeters: '))
        total_months +=1
        total_rainfall += rainfall_month

average = total_rainfall/ total_months
#display
print('Total months: '+ str(total_months))
print(f'Total rainfall: {total_rainfall} mm')
print(f'Average rainfall: {average} mm')
'''
years= int(input('Enter number of years'))
total_rainfall =0
#getting all months, need to add number of months too
total_months = 0
for n_years in range(years):
    for n_months in range(12):
            print(f'Input rainfall for '+
                f'Month {n_months+1} year {n_years+1}', end='')
            rainfall_month= float(input(' in millimeters: '))
            total_months +=1
            total_rainfall += rainfall_month

average = total_rainfall/ total_months
#display
print('Total months: '+ str(total_months))
print(f'Total rainfall: {total_rainfall} mm')
print(f'Average rainfall: {average} mm')