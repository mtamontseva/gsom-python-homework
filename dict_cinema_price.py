d = {'Паразиты': {12:250, 16:350, 20:450}, 
     '1917': {10:250, 13:350, 16:350}, 
     'Соник в кино': {10:250, 14:450, 18:450}}
film = input('Выберите фильм:')
date = input(r'Выберите дату (сегодня, завтра)')
time = int(input('Выберите время'))
tickets = int(input('Количество человек'))
if date == 'сегодня'and tickets < 20:
    print(d[film][time]*tickets, 'руб.')
elif date == 'сегодня'and tickets >= 20:
    print(d[film][time]*tickets*0.8, 'руб.')
elif date == 'завтра'and tickets < 20:
    print(d[film][time]*tickets*0.95, 'руб.')
elif date == 'завтра'and tickets >= 20:
    print(d[film][time]*tickets*0.75, 'руб.')
else:
    print('Таких вариантов покупки нет')
