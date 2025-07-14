def month_to_season(a):
    if a == 1 or a == 2 or a == 12:
        return ("Зима")
    elif a in (3, 4, 5):
        return ("Весна")
    elif a in (6, 7, 8):
        return ("Лето")
    elif a in (9, 10, 11):
        return ("Осень")
    else:
        return ("Укажите правильный номер месяца")


print(month_to_season(int(input("Введите номер месяца "))))
