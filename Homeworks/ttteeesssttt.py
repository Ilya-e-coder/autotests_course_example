# Статистика букв
# Напишите функцию letter_stat, которая на вход принимает строку our_str и возращает словарь letters_dict,
# где в качестве ключей буквы строки, а значениями являются числа,
# соответствующие количеству вхождений данной буквы в строку.
# Например (Ввод --> Вывод) :
# 'letter' --> {'l': 1, 'e': 2, 't': 2, 'r': 1}

a = 'letter'
x = {a[i]: a.count(a[i]) for i in range(len(a))}
print(x)
# k = []
# v = []
# for i in range(len(a)):
#     k.append(a[i])
#     v.append(a.count(a[i]))
# print(k)
# print(v)
# x = dict.fromkeys(k, v)
# print(x)
