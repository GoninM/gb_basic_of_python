"""
2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
    Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
"""

import random


def GetRndElement(in_list):
    if len(in_list):
        return random.choice(in_list)

    return None


Some_list = [1, 2, 3, 4, 6, 7, 3, 4, 6, 99]
EmptyList = []
print(GetRndElement(EmptyList))
