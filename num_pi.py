import math
digits = int(input('Введите число знаков после запятой:'))
print('{number:.{digits}f}'.format(number = math.pi, digits = digits))
