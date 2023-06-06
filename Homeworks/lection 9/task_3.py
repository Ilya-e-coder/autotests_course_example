# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path

work_dir = Path.cwd()
sub_dir_prices = Path(work_dir, 'test_file/task_3.txt')

open_sub_dir_prices = open(sub_dir_prices, 'r')

with open_sub_dir_prices as prices:
    sum_prices = 0
    sum_prices_list = []

    # Генерируем список без символа перевода строки при чтении файла
    clear_prices_list = [line.rstrip() for line in prices.readlines()]

    # Складываем значения цен, до пустой строки, после чего добавляем сумму значений в новый список и обнуляем счетчик
    for price in clear_prices_list:
        if price != '':
            sum_prices += int(price)
        else:
            sum_prices_list.append(sum_prices)
            sum_prices = 0
    three_most_expensive_purchases = (sum(sorted(sum_prices_list, reverse=True)[:3]))

assert three_most_expensive_purchases == 202346
