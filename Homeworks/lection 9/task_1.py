# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
import re
from pathlib import Path

work_dir = Path.cwd()
sub_wrong_file = Path(work_dir, 'test_file/task1_data.txt')
dir_for_new_file = Path(work_dir, 'test_file/task1_answer.txt')

# Открываем файл на чтение
open_sub_wrong_file = open(sub_wrong_file, 'r', encoding='utf-8')
# Открываем (создаем) файл на запись
create_answer_file = open(dir_for_new_file, 'w', encoding='utf-8')

# Читаем каждую строку и перезаписываем в новый файл, удаляя все цифры
with open_sub_wrong_file as wrong:
    with create_answer_file as answer:
        for line in wrong.readlines():
            answer.write(re.sub(r'\d', '', line))

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
