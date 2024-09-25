from smartphone import Smartphone

catalog = []


catalog.append(Smartphone("Apple", "iPhone 14", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79161234568"))
catalog.append(Smartphone("Google", "Pixel 6", "+79161234569"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79161234570"))
catalog.append(Smartphone("Huawei", "P50 Pro", "+79161234571"))


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")
