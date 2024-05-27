from adress import Adress
from mailing import Mailing

to_adress = Adress("142000", "Домодедово", "Дружбы", "2", "109")
from_adress = Adress("148034", "Саратов", "Академическая", "10", "14")
mailing = Mailing(to_adress, from_adress, 1000, "U124HN")

print(f"Отправление {mailing.track} из {mailing.from_adress.index}, {mailing.from_adress.city}, {mailing.from_adress.street}, {mailing.from_adress.house} - {mailing.from_adress.apartment} в {mailing.to_adress.index}, {mailing.to_adress.city}, {mailing.to_adress.street}, {mailing.to_adress.house} - {mailing.to_adress.apartment}. \nСтоимость {mailing.cost} рублей.")