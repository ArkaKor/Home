from adress import Adress
from mailing import Mailing

to_adress = Adress
from_adress = Adress
to_adress = 141300, "г. Сергиев Посад", "ул. Вавилова", 12, 30
from_adress = 164212, "г. Тверь", "ул. Советская", 23, 36

sending = Mailing
sending(to_adress, from_adress, 1200, 1234567890)

print(
    "Отправление",
    sending.track,
    "из",
    from_adress,
    "в",
    to_adress,
    ". Стоимость",
    sending.cost,
    "рублей.",
)
