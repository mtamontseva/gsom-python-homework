import random

chislo = int(input('Загадайте число от 1 до 4'))
comp = random.randint(1,4)
if chislo == comp:
    print('Победа!')
elif chislo < comp:
    print('Ваше число меньше!')
else:
    print('Ваше число больше!')
