import random

print('\n\n\t\t\t Приветствую тебя храбрый Капитан!')
name = input('\n- Как тебя зовут? : ')
print('\n- Приятно познакомиться, ', name, '!')
input()

print('''      _       _
     (_\     /_)
       ))   ((
     .-"""""""-.
 /^\/  _.   _.  \/^\\
 \(   /__\ /__\   )/
  \,  \o_/_\o_/  ,/
    \    (_)    /
     `-.'==='.-'
      __) - (__
     /  `~~~`  \\
    /  /     \  \\
    \ :       ; /
     \|==(*)==|/
      :       :
       \  |  /
     ___)=|=(___
    {____/ \____}''')
input('\n\n- Ну а меня зовут Зуобик или просто "Зу" для друзей.')

print(''' - В нашей звездной системе завелись злые пираты. Они крадут наш Сыр! 
   О нем мечтал и сам Шекспир! Но жаль - ведь он штаны протер до дыр... 
 - В общем, нам нужна помощь такого крутого Звездного Капитана как ты!''')
input()

input('Выбери свой корабль:')

print('\n\t "1" Выбрать "Планетарный Эсминец":')
print('''                  ____________
          ..====``` _______  ```=====\\
     ..===``````  //@@@@@@//===={####0
      ``````````````````````````=====/''')
print('\n\n\t "2" Выбрать "Звездный Крейсер":')
print('''              ______________
          ..== ...   ... .. ==..         _______
     ..==``    ```   ```        ``==...//```````\\
     ###---=={@@@}-====-{@@@}---------//________/
     ``````\\__________________________\\\\        \\
                            \\_________//________/
''')
print('\n\t "3" Выбрать "Галактический Линкор":')
print('''                                                        |
                                     ___|_______________|__               
           <<-----------------------/<<-<<-- --  --/ <<->> \\---|-----/#####/````````\\
      ////___````````````````````````````````````````````````````````\\#####\\......../
    __________\\_______________________________//```//````//`````//`````/#####/```````\\
    ``````````<<<_____________________________\\\\___\\\\____\\\\_____\\\\_____\\#####\\......./''')

ship_type = int(input('\n\n Сделайте свой выбор: '))


if ship_type == 1:
    health = 800
    damage = 50
    print('Вы выбрали "Планетарный Эсминец" с прочностью корпуса: ', health)
    print('И мощностью выстрела: ', damage)
    print('''                  ____________
              ..====``` _______  ```=====\\
         ..===``````  //@@@@@@//===={####0
          ``````````````````````````=====/''')

elif ship_type == 2:
    health = 1500
    damage = 100
    print('Вы выбрали "Звездный Крейсер" с прочностью корпуса: ', health)
    print('И мощностью выстрела: ', damage)
    print('''                  ______________
              ..== ...   ... .. ==..         _______
         ..==``    ```   ```        ``==...//```````\\
         ###---=={@@@}-====-{@@@}---------//________/
         ``````\\__________________________\\\\        \\
                                \\_________//________/
    ''')

else:
    health = 2500
    damage = 200
    print('Вы выбрали "Галактический Линкор" с прочностью корпуса: ', health)
    print('И мощностью выстрела: ', damage)
    print('''                                                        |
                                     ___|_______________|__               
           <<-----------------------/<<-<<-- --  --/ <<->> \\---|-----/#####/````````\\
      ////___````````````````````````````````````````````````````````\\#####\\......../
    __________\\_______________________________//```//````//`````//`````/#####/```````\\
    ``````````<<<_____________________________\\\\___\\\\____\\\\_____\\\\_____\\#####\\......./''')


max_hull = health
print('\n\n- Отличный выбор, ', name, '!')
input()

print('\a')
print(''' - И очень вовремя! Мы видим приближающийся космический корабль Пиратов! 
Они снова пришли за Сыром! Защитите наш Сыр и Родина вас не забудет!''')
input()

print(name, ''': 
- Запускаем двигатели!''')
input('- Выходим на курс перехвата пиратов!')
print('- Капитан', name, 'снова в деле!')
input('- Всем приготовиться! Начинается сражение! \n\n')

pirate_health = 1000
pirate_shot = 100

while health >= 1 and pirate_health >= 1:
    health = health - pirate_shot
    pirate_health = pirate_health - damage
    print('Пираты стреляют по вашему кораблю на: ', pirate_shot, ' урона')
    print('\t У вашего корабля остается: ', health, 'очков прочности')
    print('Ваш корабль стреляет по кораблю пиратов на: ', damage, ' урона')
    print('\t У корабля Пиратов остается: ', pirate_health, 'очков прочности')
    input()

if health > pirate_health:
    input(' - Ура! Вы победили! Наш Сыр спасён!')
    print('''
                                 .''.
       .''.             *''*    :_\\/_:     . 
      :_\\/_:   .    .:.*_\\/_*   : /\\ :  .'.:.'.
  .''.: /\\ : _\\(/_  ':'* /\\ *  : '..'.  -=:o:=-
 :_\\/_:'.:::. /)\\*''*  .|.* '.\\'/.'_\\(/_'.':'.'
 : /\\ : :::::  '*_\\/_* | |  -= o =- /)\\    '  *
  '..'  ':::'   * /\\ * |'|  .'/.\\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
    print('\a')

    input('\n\t\t Welcome to funny repairs!')
    print('\n- Welcome, ', name,'! Welcome my friend!')
    input('- Let\'s repair your ship after battle!')

    # temp. offline
    # health = int(input('\n Set your ship hull remaining hp:'))
    # while health <= 0 or health >= 2401:
    #    print('\n The number is wrong. Try number from 1 to 2400.')
    #    health = int(input('\n Set your ship hull remaining hp:'))

    print('\n Your ship is ', health, ' hp strong now.')
    print(' Now repairs are starting! \n')
    input()

    while True:
        drunk_chance = random.randrange(0, 16)
        health += 50
        print('After repairs your ship hull is', health, 'hp')
        if drunk_chance == 10:
            print('\n Zuobik is too drunk with "Cheezy beer".')
            input('Tap him on his shoulder to wake him up ;)\n')
            continue
        elif health >= max_hull:
            break
    print('\n Your hull reached: ', health, ' out of ', max_hull, ' hp.')
    input('\nNow that your ship is fixed, you\'re ready for a new journey!\n')

else:
    input('Ваш корабль был уничтожен!')

    print('''
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
''')
    print('\a')
input('Конец игры!')
