def showmenu():
    print('''\tCSV MANAGER
    1. Создать .csv
    2. поиск элемента в файле
    3. Сортировка данных
    4. Добавление данных в файл
    5. Удаление данных из файла
    6. Добавление элементов в группу
    7. Вывести файл
    ''')
def choice_menu():
    try:
        choice=int(input('Введите число: '))
        if 1>choice or choice>7: raise ValueError('некорректные данные')
        else: return choice
    except  Exception:
        raise ValueError('некорректные данные')
def show_data(input_str):
    for i in input_str.split('\n'):
        for j in i.split(';'):
            print(j, end="\t\t\t")
        print()


