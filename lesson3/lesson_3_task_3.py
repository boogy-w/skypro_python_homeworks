from address import Address
from mailing import Mailing


to_address = Address("123456", "Москва", "Арбат", "10", "15")
from_address = Address("654321", "Санкт-Петербург", "Невский проспект", "25", "30")


mailing = Mailing(to_address=to_address, from_address=from_address, cost=500, track="TR12345RU")


print(mailing)
