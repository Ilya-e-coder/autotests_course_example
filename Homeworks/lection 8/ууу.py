from pathlib import Path

work_dir = Path.cwd()
print(work_dir)
print('______' * 7)

path = Path('sub', '21.txt')
print(path)
print('______' * 7)

abs_path = Path(Path.cwd(), path)
abs_path1 = Path(work_dir, path)
print('1 - ', abs_path)
print('2 - ', abs_path1)

f = open('ex1.txt')
fp = open('C:\\autotests_course\Homeworks\lection 8\sub\\21.txt', 'r', encoding='utf-8')
# print(*f)
print(*fp)

print(f.read(3))
print(f.read(3))
print(f.read(3))
print(f.tell())
f.seek(0)
print(f.read(3))
print('______' * 7)
x = open('ex1.txt')
for i in x.readlines():
    print(i, end='')
print('______' * 7)

# write
# file = open('new.txt', 'w', encoding='utf-8')
# file.write('Привет, медвед')
# file = open('new.txt', 'w', encoding='utf-8')
# file.write('Прощай, медвед')
try:
    with open('new.txt', mode='w+', encoding='utf-8') as file:
        # file.writelines(['gfweweg\n', '3gergererhvcccv\n'])
        file.seek(0)
        print(file.read())
        assert False
finally:
    print(file.closed)
    # file.seek(0)
    # print(file.read(7))
    # print(file.read(7))
#     file.write('Привет, медвед')
    # file.write('Прощай, медвед')
# file = open('new.txt', 'r', encoding='utf-8')
# print(file.read())
#
# gol = work_dir.glob('**/*.txt')
# for i in gol:
#     print(i)







