from address import Address
from mailing import Mailing

sending = Mailing(Address(141300, "г. Сергиев Посад", "ул. Вавилова", 12, 30),
                  Address(164212, "г. Тверь", "ул. Советская", 23, 36),
                  "1300", "1224567890")

print(f"Отправление {sending.track_1} из {sending.from_address_1} \
в {sending.to_address_1}. Стоимость {sending.cost_1} рублей.")
