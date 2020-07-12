user_str = input("Введите несколько слов, разделённых пробелами: ")
word_list = user_str.split()
for i in range(len(word_list)):
    print(f"{i + 1}-е слово: {word_list[i]}")