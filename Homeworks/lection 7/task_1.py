# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False

# Здесь пишем код
from math import hypot


class Segment:
    """
    Класс Segment используется для определения отрезка из точек

    :dots_1: кортеж с координатами точек (x1, y1)
    :dots_2: кортеж с координатами точек (x2, y2)
    """

    def __init__(self, dots_1, dots_2):

        self.x_1 = dots_1[0]
        self.y_1 = dots_1[1]
        self.x_2 = dots_2[0]
        self.y_2 = dots_2[1]

    def length(self):
        """
        Возвращает длину отрезка, с округлением до 2 знаков после запятой
        """

        return round(hypot(self.x_2 - self.x_1, self.y_2 - self.y_1), 2)

    def x_axis_intersection(self):
        """
        True, если отрезок пересекает ось абцисс, иначе False
        """
        if (self.x_1 >= 0 and self.x_2 <= 0) or (self.x_1 <= 0 and self.x_2 >= 0):
            return True
        else:
            return False

    def y_axis_intersection(self):
        """
        True, если отрезок пересекает ось ординат, иначе False
        """

        if (self.y_1 >= 0 and self.y_2 <= 0) or (self.y_1 <= 0 and self.y_2 >= 0):
            return True
        else:
            return False


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]

test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
