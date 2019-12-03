import sys

star = '**'

appetizers = { 'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0 }
entrees = {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden': 0 }
desserts = {'Ice Cream': 0, 'Cake': 0, 'Pie': 0 }
drinks = {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0 }

print(star * 19)
print(f'{star} Welcome to the Snakes Cafe! {star}')
print(f'{star} Please see our menu below. {star}')
print(f'{star}')
print(f'{star} To quit at any time, type "quit" {star}')
print(star * 19)
print('')

print('Appetizers\n----------')
for key,value in appetizers.items():
  print(key)
print('')


print('Entrees\n-------')
for key,value in entrees.items():
  print(key)
print('')


print('Desserts\n--------')
for key,value in desserts.items():
  print(key)
print('')


print('Drinks\n------')
for key,value in drinks.items():
  print(key)
print('')

print(star * 19)
print(f"{star} What would you like to order? {star}")
print(star * 19)


while True:
    answer = input()

    if answer in appetizers:
      appetizers[answer] += 1
      print(f'{star} {appetizers[answer]} order of {answer} have been added to your meal {star}')

    if answer in entrees:
      entrees[answer] += 1
      print(f'{star} {entrees[answer]} order of {answer} have been added to your meal {star}')

    if answer in desserts:
      desserts[answer] += 1
      print(f'{star} {desserts[answer]} order of {answer} have been added to your meal {star}')

    if answer in drinks:
      drinks[answer] += 1
      print(f'{star} {drinks[answer]} order of {answer} have been added to your meal {star}')

    if answer == 'quit':
      print('Thank you for your order!')
      sys.exit()
