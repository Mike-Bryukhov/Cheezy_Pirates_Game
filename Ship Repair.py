# "Funny repairs" program
# Usage of randomly generated numbers as a cycle breaker.

import random

print('\n Welcome to funny repairs!')

ship_hull = int(input('\n Set your ship hull remaining hp:'))

while ship_hull <= 0 or ship_hull >= 2401:
    print('\n The number is wrong. Try number from 1 to 2400.')
    ship_hull = int(input('\n Set your ship hull remaining hp:'))

print('\n Your ship is ', ship_hull,' hp strong now.')
input()

max_hull = 2400

print('Now repairs are starting!')

while True:
    drunk_chance = random.randrange(0, 21)
    ship_hull += 50
    print('After repairs your ship hull is', ship_hull, 'hp')
    if drunk_chance == 5:
        print('\n Zuobik is too drunk with "Cheezy beer".')
        input('Tap him on his shoulder to wake him up ;)')
        continue
    elif ship_hull >= max_hull:
        break
print('\n Your hull reached: ', ship_hull, ' out of ', max_hull, ' hp.')
input()
