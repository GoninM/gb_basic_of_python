"""
1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
    Примечание: Списки фруктов создайте вручную в начале файла.
"""

list_1 = ["яблоко", "апельсин", "мандарин", "банан"]
list_2 = ["дыня", "яблоко", "арбуз", "слива", "мандарин", "банан"]

result = [fruite for fruite in list_1 if list_2.count(fruite)]

print(result)

