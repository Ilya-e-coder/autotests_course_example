# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

# Здесь пишем код
class RomanNums:

    def __init__(self, number):
        self.number = number


    def from_roman(self):
        arab_numbs_list = []

        for letter in range(0, len(self.number)):
            if self.number[letter] == 'I':
                arab_numbs_list.append(int(1))
            elif self.number[letter] == 'V':
                arab_numbs_list.append(int(5))
            elif self.number[letter] == 'X':
                arab_numbs_list.append(int(10))
            elif self.number[letter] == 'L':
                arab_numbs_list.append(int(50))
            elif self.number[letter] == 'C':
                arab_numbs_list.append(int(100))
            elif self.number[letter] == 'D':
                arab_numbs_list.append(int(500))
            elif self.number[letter] == 'M':
                arab_numbs_list.append(int(1000))
        return sum(arab_numbs_list)


    def is_palindrome(self):
        arab_numbs_list = []

        for letter in range(0, len(self.number)):
            if self.number[letter] == 'I':
                arab_numbs_list.append(int(1))
            elif self.number[letter] == 'V':
                arab_numbs_list.append(int(5))
            elif self.number[letter] == 'X':
                arab_numbs_list.append(int(10))
            elif self.number[letter] == 'L':
                arab_numbs_list.append(int(50))
            elif self.number[letter] == 'C':
                arab_numbs_list.append(int(100))
            elif self.number[letter] == 'D':
                arab_numbs_list.append(int(500))
            elif self.number[letter] == 'M':
                arab_numbs_list.append(int(1000))
        polin = sum(arab_numbs_list)
        assert polin[:] == polin[::-1], False

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]


test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
