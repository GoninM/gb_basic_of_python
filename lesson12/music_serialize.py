"""
1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы,
например:
my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}

С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
вывести результаты в терминал. Записать результаты в файлы group.json, group.pickle соответственно.
В файле group.json указать кодировку utf-8.
"""
import json
import pickle


my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
{'name': 'Шапито', 'year': 2014}]}

json_str = json.dumps(my_favourite_group)
print(json_str)

pickle_str = pickle.dumps(my_favourite_group)
print(pickle_str)

with open('group.json', 'w', encoding='utf-8') as f:
    f.write(json_str)

with open('group.pickle', 'wb') as f:
    f.write(pickle_str)