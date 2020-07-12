list_of_diff_type = [3, 46.834, 5 + 6j, " Hello, world", [1, 78, "Hi", False], (1, 78, "Hi", False), {1, 78, "Hi", False}, {"apple": "яблоко", "food": "еда"}, True, b'text', None]
for i in list_of_diff_type:
    print(f"{i}: {type(i)}")