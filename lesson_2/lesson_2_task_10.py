def bank(x,y):
    x = int(x)
    y = int(y)
    balance = x * (1.1 ** y)
    balance = round(balance,2)
    return balance

print(bank(input("Введите сумму"),input("Введите количество лет")))

