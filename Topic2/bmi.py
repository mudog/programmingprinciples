'''
BMI = weight X 703/ (height**2)
enter weight
enter height
calculate BMI
display BMI
if BMI >=18.5 and BMI <25 optimal
if BMI <18.5 underweight
if BMI >25 overweight
BMIclass
'''
weight = int(input('insert weight in pounds: '))
height = int(input('insert height in inches: '))

#BMI calc
bmi= weight * 703 / (height**2)
#display BMI
print('BMI: '+ format(bmi,'.1f'))
#BMI class
bmi_class= 'unknown'
if bmi >25:
    bmi_class = 'Overweight'
elif bmi <18.5:
    bmi_class = 'Underweight'
else:
    bmi_class = 'Optimal'

#display bmi class
print(f'Your BMI is {bmi_class}')