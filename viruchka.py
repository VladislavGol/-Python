revenue = int(input("Введите значение выручки: "))
cost = int(input("Введите значение издержек: "))
if revenue < cost:
    print("Вы ушли в убыток")
elif revenue > cost:
    workers = int(input("Вы ушли в прибыль. Введите число сотрудников: "))
    profit = revenue - cost
    profit_per_worker = profit / workers
    print(f"Ваша общая прибыль составила: {profit}")
    print(f"Ваша прибыль на одного работника составила: {profit_per_worker}")