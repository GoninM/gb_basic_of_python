'''
1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
 Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
'''

import os


def Create10Dir():
    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            print('папка уже существует')
        finally:
            None


def Remove10Dir():
    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        os.rmdir(dir_name)


if __name__ == '__main__':
    Create10Dir()
    Remove10Dir()
