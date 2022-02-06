import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info

save_info('start')

command = ""
try:
    command = sys.argv[1]
except IndexError:
    print("Enter command")

if command == "list":
    get_list()
elif command == "create_file":
    try:
        name = sys.argv[2]
        create_file(name)
    except IndexError:
        print("enter file name")
elif command == "create_folder":
    try:
        name = sys.argv[2]
        create_folder(name)
    except IndexError:
        print("enter folder name")
elif command == "delete":
    try:
        name = sys.argv[2]
        delete_file(name)
    except IndexError:
        print("enter file/folder name")
elif command == "copy":
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
        copy_file(name, new_name)
    except IndexError:
        print("enter source file name and new file name")
elif command == "help":
    print("list - ")
    print("create_file name")
    print("create_folder")
    print("delete")
    print("copy")

save_info('End')
