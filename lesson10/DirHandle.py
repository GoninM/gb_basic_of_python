import os


def Create10Dir():
    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        #print(dir_name)
        try:
            os.mkdir(dir_name)
        except(FileExistsError):
            print('папка уже существует')
        finally:
            None

def Remove10Dir():
    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        #print(dir_name)
        os.rmdir(dir_name)



#Create10Dir()
#Remove10Dir()
