s = '''В разные эпохи и у разных народов число Пи имело разное значение. Например, в
Древнем Египте оно равнялось 3.1604 у индусов оно приобрело значение 3.162 китайцы
пользовались числом, равным 3.1459 Буквенное обозначение число Пи получило только
в 1706 году – оно происходит от начальных букв двух греческих слов, означающих
окружность и периметр. Буквой π число наделил математик Джонс, а прочно вошла в
математику она уже в 1737 году.'''
summa = 0
counter = 0
spisok = []
l = s.split(' ')
for st in l:
    if (st.replace('.','')).isdigit():
        summa = summa + float(st)
        counter = counter + 1
        spisok.append(float(st))
print(summa)
print(counter)
print(max(spisok))
