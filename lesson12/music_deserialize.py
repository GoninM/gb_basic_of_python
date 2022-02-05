"""
2: Создать модуль music_deserialize.py.
В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
И получить объект: словарь из предыдущего задания.
"""
import json
import pickle

json_str = ''
pickle_str = ''


with open('group.json', 'r', encoding='utf-8') as f:
    json_str = json.load(f)

print(json_str)
print(type(json_str))

with open('group.pickle', 'rb') as f:
    pickle_str = pickle.load(f)

print(pickle_str)
print(type(pickle_str))
