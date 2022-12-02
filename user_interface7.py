import file_writer7 as fw
import file_reader7 as fr
import os

filename = "myphonebook.txt"


def export_to_file():
    Export_filename = input(
        'Укажите имя файла в который будем экспортировать информацию из справочника     ')
    while True:
        Format_file = input(
            'Укажите формат файла в который будем экспортировать информацию из справочника (1- txt, 2 - csv)      ')
        if Format_file == '1':
            Export_filename += '.txt'
            break
        elif Format_file == '2':
            Export_filename += '.csv'
            break
        else:
            print("Выберети цифру из указанных\n")


def import_from_file():
    Import_filename = input(
        'Укажите имя файла из которого будем импортировать информацию из справочника     ')
    while True:
        Format_file = input(
            'Укажите формат файла из которого будем импортировать информацию из справочника (1- txt, 2 - csv)      ')
        if Format_file == '1':
            Import_filename += '.txt'
            break
        elif Format_file == '2':
            Import_filename += '.csv'
            break
        else:
            print("Выберети цифру из указанных\n")

    filecontents = fr.reader(Import_filename)
    fw.writing_to_file(filecontents, filename)
    print("Загрузка в базу выполнена")


def main_menu():
    os.system('cls')
    global filename

    print("\nГлавное меню\n")
    print("1. Показать все записи справочника")
    print("2. Добавить запись")
    print("3. Найти запись")
    print("4. Экспорт в файл")
    print("5. Импорт из файла")
    print("6. Выход")
    choice = input("Сделайте выбор: ")
    if choice == "1":
        filecontents = fr.reader(filename)
        if len(filecontents) == 0:
            print("Нет записей")
        else:
            print(filecontents)
        enter = input("Нажмите для продолжения ...")
        main_menu()
    elif choice == "2":
        newcontact(filename)
        enter = input("Нажмите для продолжения ...")
        main_menu()
    elif choice == "3":
        searchcontact(filename)
        enter = input("Нажмите для продолжения ...")
        main_menu()
    elif choice == "4":
        export_to_file()
        enter = input("Нажмите для продолжения ...")
        main_menu()
    elif choice == "5":
        import_from_file()
        enter = input("Нажмите для продолжения ...")
        main_menu()
    elif choice == "6":
        print("Выхожу...")
    else:
        print("Выберети цифру из указанных\n")
        enter = input("Нажмите для продолжения ...")
        main_menu()

# defining search function


def searchcontact(filename):
    searchname = input("Укажите фамилию или имя для поиска: ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    myfile = open(filename, "r+")
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print("Найдена запись :    ", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print("Записи согласно введному запросу не найдены  ", searchname)

# first name


def input_firstname():
    first = input('Введите имя: ')
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname

# last name


def input_lastname():
    last = input("Введите фамилию: ")
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname

# storing the new contact details


def newcontact(filename):
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Введите номер телефона: ")
    AnotherInf = input("Введите описание: ")
    contactDetails = ("[" + firstname + " " + lastname +
                      ", " + phoneNum + ", " + AnotherInf + "]\n")
    fw.writing_to_file(contactDetails, filename)
    #myfile = open(filename, "a")
    # myfile.write(contactDetails)
    print("Следующая информация:\n " +
          contactDetails + "\nбыла сохранена")
