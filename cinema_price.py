film = input('Выберите фильм:')
date = input(r'Выберите дату (сегодня, завтра)')
time = int(input('Выберите время'))
tickets = int(input('Количество человек'))
if film == 'Паразиты':
    if time == 12:
        my_price = 250
    elif time == 16:
        my_price = 350
    elif time == 20:
        my_price = 450
    else:
        print('Такого времени нет')
elif film == '1917':
    if time == 10:
        my_price = 250
    elif time == 13:
        my_price = 350
    elif time == 16:
        my_price = 350
    else:
        print('Такого времени нет')
elif film == 'Соник в кино':
    if time == 10:
        my_price = 250
    elif time == 14:
        my_price = 450
    elif time == 18:
        my_price = 450
    else:
        print('Такого времени нет')
else:
    print('Такого фильма нет')
if date == 'сегодня'and tickets < 20:
    print(my_price*tickets, 'руб.')
elif date == 'сегодня'and tickets >= 20:
    print(my_price*tickets*0.8, 'руб.')
elif date == 'завтра'and tickets < 20:
    print(my_price*tickets*0.95, 'руб.')
elif date == 'завтра'and tickets >= 20:
    print(my_price*tickets*0.75, 'руб.')
else:
    print('Таких вариантов покупки нет')
