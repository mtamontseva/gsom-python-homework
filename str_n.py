s = str(input('Введите строку:'))
n = int(input('Введите число:'))
def func(s, n):
    if len(s) > n:
        return(s.upper())
    else:
        return(s)
func(s, n)
