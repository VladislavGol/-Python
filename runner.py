start_result = int(input("Введите расстояние в первый день пробежки: "))
finish_result = int(input("Введите целевое расстояние: "))
day = 1
while start_result < finish_result:
    start_result *= 1.1
    day += 1
print(f"на {day}-й день спортсмен достиг результата — не менее {finish_result} км.")