user_list = []
num = int(input("Введите количество элементов списка: "))
for i in range(num):
    el = input(f"Введите значение {i + 1}-ого элемента списка: ")
    user_list.append(el)
if num % 2 == 0:
    for j in range(0, len(user_list), 2):
        save_el = user_list[j]
        user_list[j] = user_list[j +1]
        user_list[j + 1] = save_el
elif num % 2 == 1:
    save_end_el =  user_list[-1]
    user_list.pop(-1)
    for j in range(0, len(user_list), 2):
        save_el = user_list[j]
        user_list[j] = user_list[j +1]
        user_list[j + 1] = save_el
    user_list.append(save_end_el)
print("Ваш получившийся список: ")
for i in range(len(user_list)):
    print(f"Значение {i + 1}-ого элемента списка: {user_list[i]}")

