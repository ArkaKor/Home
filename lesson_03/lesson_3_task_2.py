from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Mi 10", "+7 913 867 36 59"),
    Smartphone("LG", "L 20", "+7 937 477 23 30"),
    Smartphone("Samsung", "Galaxy 10", "+7 954 567 02 43"),
    Smartphone("Sony", "Xperia X5", "+7 933 719 23 75"),
    Smartphone("Google", "Pixel 8", "+7 914 625 90 34")
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
