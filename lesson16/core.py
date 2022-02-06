import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Такая папка уже есть")


def get_list(folder_only=False):
    result = os.listdir()
    if folder_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print("файл/папка не найдены")


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("такая папка уже есть")
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f"{current_time}: {message}"

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(result + "\n")


if __name__ == '__main__':
    create_file('testfile.dat')
    create_file('testfile2.dat')
    create_file('testfile.dat', 'some text')

    create_folder('test folder')

    get_list()
    get_list(True)

    delete_file('test folder')
    delete_file('test folder')
    delete_file('testfile.dat')

    create_folder('test folder2')
    copy_file('test folder2', 'test folder3')

    copy_file('testfile2.dat', 'testfile3.dat')

    save_info('test')
