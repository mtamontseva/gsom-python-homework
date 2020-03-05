value = input("Введите атомный номер: ")
if value:
    number = int(value)
    if number == 3:
        print("Литий")
    elif number == 12:
        print("Магний")
    elif number == 17:
        print("Хлор")
    elif number == 80:
        print("Ртуть")
    else:
        print("Что это?!")
else:
    print("Введите атомный номер!")
    
