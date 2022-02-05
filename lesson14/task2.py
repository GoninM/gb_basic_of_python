"""
2: Дан список, заполненный произвольными числами. Получить список из элементов исходного,
удовлетворяющих следующим условиям:
Элемент кратен 3,
Элемент положительный,
Элемент не кратен 4.

Примечание: Список с целыми числами создайте вручную в начале файла.
Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
"""

rnd_list = [-1, -5, -76, 0, 100, 34, 12, 33, 1, 99, -1000]

result1 = [number for number in rnd_list if number % 3 == 0]
print(result1)

result2 = [number for number in rnd_list if number >= 0]
print(result2)

result3 = [number for number in rnd_list if number % 4 != 0]
print(result3)

result4 = [number for number in rnd_list if (number % 3 == 0) and (number >= 0) and (number % 4 != 0)]
print(result4)
