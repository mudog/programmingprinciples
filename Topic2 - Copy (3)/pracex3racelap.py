'''
enter number of laps
loop prompt to enter lap time for each lap
definite loop for statement
runnin total loop count

when loop finish display fastest lap time
display slowest lap time
display average lap time
'''
laps = int(input('Enter number of laps: '))
#time - each iteration

#running total - sum
sum = 0
#runnig variable - slowest
slowest = 0
#running variable - fastest, upper limit
fastest = 99999

#for loop - sum to use for average calculation
for number in range(laps):
    print('Lap '+str(number)+';')
    time = float(input('Time for lap'))
    sum += time
#loop condition - slowest
    if slowest < time:
        slowest = time
#loop condition - fastest
    if fastest > time:
        fastest = time
#average calc
average = sum/laps




print('Slowest lap ' + str(slowest)
      )
print('Fastest lap ' + str(fastest)
      )
print('Average lap ' + str(average)
      )

