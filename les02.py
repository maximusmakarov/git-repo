import os
import sys
import shutil
import psutil

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл" + newfile + "был успешно создан.")
            return True
        else:
            print("Возникли проблемы копирования")
            return False

def sys_info():
    print(os.name)
    print("Тукущая директория: ", os.getcwd())
    print("Платформа на которой работает интерпретатор: ", sys.platform)
    print("Версия интерпретатора: ", sys.version)
    print("Кодировка: ", sys.getfilesystemencoding())
    print("Логин пользователя: ", os.getlogin())
    print("Количество ядер CPU: ", psutil.cpu_count())


print("Great Python Program!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = ''
while answer != 'Q':
    answer = input("Давайте поработаем? (Y/N/Q)")
    if answer == 'Y':
        print("Отлично, хозяин!")
        print("Я умею:")
        print(" [1] - выведу список файлов")
        print(" [2] - выведу информацию о системе")
        print(" [3] - выведу список процессов")
        print(" [4] - продублирую файлы в текущей директории")
        print(" [5] - удалю все продублированные файлы в текущей директории")
        print(" [6] - продублирую указанный файл в текущей директории")
        print(" [7] - удалю указанный файл в указанной директории")
        do = int(input("Укажите номер действия: "))

        if do == 1:
            print(os.listdir())
        elif do == 2:
            sys_info()

        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            file_list = os.getcwd()
            i = 0
            newFile = ""
            while i < len(file_list):
                duplicate_file()
            print("Все файлы в текущей директории продублированы")
        elif do == 5:

            print("удалю все продублированные файлы в текущей директории")
            dirname = input("Укажите имя директории:")
            file_list = os.listdir(dirname)

            for f in file_list:
                fullname = os.path.join(dirname, f)
                if fullname.endswith(".dupl"):
                    os.remove(fullname)  # i +=1

        elif do == 6:
            print("Продублирую указанный файл в текущей дериктории")
            print(os.listdir())
            filename = input("Укажите имя файла: ")
            duplicate_file(filename)

        else:
            pass

    elif answer == 'Q':
        print("До свидания!")
    else:
        print("Неизвестный ответ")
