year = input("Введите год: ")
year_num = int(year)

for n in [year_num]:
    if (n % 4 == 0):
        print(True)
    else:
        print(False)
