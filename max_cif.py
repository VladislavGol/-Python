user_number = int(input("Введите любое положительное число: "))
number = user_number
max = 0
while number > 0:
    figure = number % 10
    if figure > max:
        max = figure
    number //= 10

print(f"Максимальна цифра в числе {user_number}: {max}")
