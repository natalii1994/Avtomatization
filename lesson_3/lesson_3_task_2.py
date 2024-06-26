from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Sumsung","Galaxy S20","+79990000000")
phone2 = Smartphone("Sumsung","Galaxy S23","+79000000000")
phone3 = Smartphone("Apple","iPhone 15 Pro Max","+79155555555")
phone4 = Smartphone("Google","Pixel 7","+79166666666") 
phone5 = Smartphone("Poco","X6 Pro","+79177777777") 

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")




