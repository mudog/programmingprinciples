'''
number of male and female registered in a class
display as percentage

#get number in class total - for sake of simplicity- male + female
get number of males
get number of females
calculate total - male + female
calculate percentage male - male / total * 100
calculate percentage female - female / total * 100
display percent
'''
male = int(input('How many males?: '))
female = int(input('How many females?: '))
total = male + female
_maleperc = 100 * male // total  # floor division does not work \
#with parentheses across both sides of the operator
#e.g. _maleperc = 100 * (male // total) - will not work results 0
_femaleperc = (100* female) // total

display = print('The class is ' + str(_maleperc)+' % male and '+
               str(_femaleperc) + ' % female.')