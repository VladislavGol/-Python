ranked_list = [7, 5, 3, 3, 2]
ranked_el = int(input("Введите новый элемент рейтинга: "))
i = 0
while (ranked_el < ranked_list[i]) and (i < (len(ranked_list) - 1)):
    i +=1
if ranked_el < ranked_list[-2]:
    ranked_list.append(ranked_el)
else:
    ranked_list.insert(i, ranked_el)
print(ranked_list)
