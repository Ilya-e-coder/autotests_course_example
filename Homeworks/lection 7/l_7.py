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
        self.arabic_numb = None


    def from_roman(self, number):
        arab_mumbs_list = []

        for letter in range(0, len(number)):
            if number[letter] == 'I':
                arab_mumbs_list.append(int(1))
            elif number[letter] == 'V':
                arab_mumbs_list.append(int(5))
            elif number[letter] == 'X':
                arab_mumbs_list.append(int(10))
            elif number[letter] == 'L':
                arab_mumbs_list.append(int(50))
            elif number[letter] == 'C':
                arab_mumbs_list.append(int(100))
            elif number[letter] == 'D':
                arab_mumbs_list.append(int(500))
            elif number[letter] == 'M':
                arab_mumbs_list.append(int(1000))
        self.arabic_numb = sum(arab_mumbs_list)

        return self.arabic_numb

    def is_palindrome(self, arabic_numb):
        polin = str(arabic_numb)
        assert polin[:] == polin[::-1], False



#
#
#
# def to_roman(number):
#     roman = ''
#     for letter, value in roman_numbers.items():
#         while number >= value:
#             roman += letter
#             number -= value
#     return roman
#
#
# print("1777 =", to_roman(1777))


# class Car:
#     age = 12
#
#     def __init__(self, model):
#         self.model = model
#
#     def info(self):
#         global age
#         print(self.model)
#         print(age)
#
#
# a = Car('BMW')
# a.info()
