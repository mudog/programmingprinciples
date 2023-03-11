'''
hot dogs package - 10
hot dog buns package - 8

enter number of people
enter number of hot dogs per person
calculate total hotdogs

calculate minimum number of packages of dogs - total / 10
calculate minimum number of packages of buns - total /8
calculate hot dogs left over -total % 10
calculate buns left over  -total % 8
display
'''
#get number of people
n_people= int(input('How many people? '))
#get hot dogs per person
hd_per_person= int(input('How many hotdogs per person? '))
#calc total hotdogs
hd_total= n_people * hd_per_person

#calculate minimum number of packages of dogs - total / 10
packs_d= hd_total // 10
#calculate minimum number of packages of buns - total /8
packs_b= hd_total // 8

#calculate hot dogs left over -total % 10
lefto_d= hd_total % 10
#calculate buns left over  -total % 8
lefto_b= hd_total % 8
#display
print(f'Number of hotdogs :{hd_total}\n' +
      f'minimum packages of hot dogs: {packs_d}\n' +
      f'minimum packages of buns: {packs_b}\n' +
      f'Leftover hot dogs: {lefto_d}\n' +
      f'Leftover buns: {lefto_b:.5f}')