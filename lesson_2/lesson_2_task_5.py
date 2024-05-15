def month_to_season(num_month):
    num_month = int(num_month)

    if num_month > 12 or num_month < 1:
        print("Такого месяца не существует")
    elif num_month >= 3 and num_month <= 5:
        print("Весна")
    elif num_month >= 6 and num_month <= 8:
        print("Лето")
    elif num_month >= 9 and num_month <= 11:
        print("Осень") 
    else:
        print("Зима") 

print(month_to_season(input("Введите номер месяца: ")))
