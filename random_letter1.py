import random
spisok = ['самовар', 'весна', 'лето']
slovo = spisok[random.randint(0,2)]
bukva_index = random.randint(0, (len(slovo) - 1))
bukva = slovo[bukva_index]
spisok = list(slovo)
spisok[bukva_index] = '?'
slovo_v = ''.join(spisok)
ugad = str(input(f'Угадай букву в слове {slovo_v}'))
if ugad == bukva:
    print(f'Победа! Слово: {slovo}')
else:
    print(f'Попробуй в другой раз! Слово: {slovo}')
