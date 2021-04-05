receipt = int(input("Введите выручку: "))
cost = int(input("Введите расходы: "))
income = (receipt - cost)
if receipt > cost:
    size = int(input("Введите численность персонала: "))
    print("Прибыль есть,можно поесть")
    print("Рентабильность фирмы составляет :", income / receipt, "%")
    print("Каждый сотрудник принес прибыль :", income / size)
elif cost > receipt:
    print("Что-то явно не так")
else:
    print("Вы работатее в ноль")