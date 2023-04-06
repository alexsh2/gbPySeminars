# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных
import re

import pandas as pd


def read_file(flname):
    with open(flname, 'r') as data:
        data_array = []
        for line in data:
            line = re.sub(r'\s+', ' ', line)
            item = line.replace('\n', '').split(sep=',')
            data_array.append(item)
    return data_array


def write_file(flname, data_array):
    with open(flname, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')


def add_item(flname, lastname='', firstname='', secondname='', phone=''):
    data_array = read_file(flname)
    max_id = 0
    for i in range(1, len(data_array)):
        if max_id < int(data_array[i][0]):
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    write_file(flname, data_array)


def show_all_items(flname):
    df = pd.read_csv(flname, sep=",", skiprows=1, skipinitialspace=True,
                     names=["ID", "Фамилия", "Имя", "Отчество", "Телефон"])
    pd.set_option('display.max_columns', None)
    print(df)


def search_for_record(flname, selection, old_string):
    data_array = read_file(flname)
    res = False
    index = []
    for i in range(1, len(data_array)):
        if data_array[i][selection].strip() == old_string:
            index.append(i)
            res = True
    if res == False:
        print('Запись с такими данными не найдена')
        return res, []
    else:
        return res, index


def list_records(data_array, index):
    ind = 0
    print('Следующие записи соответствуют поисковому запросу:')
    for i in range(len(index)):
        print(data_array[index[i]])

    id = input('Введите ID нужной записи: ')
    count = 0
    while count == 0:
        for i in range(len(index)):
            if id == (data_array[index[i]][0]):
                ind = index[i]
                count += 1
                break
        if count == 0:
            id = input('Введён неверный ID. Попробуйте ещё раз: ')
    return ind, id


def update_record(flname, index, old_item, new_item, user_selection):
    data_array = read_file(flname)
    if len(index) > 1:
        ind, id = list_records(data_array, index)
    else:
        id = (data_array[index[0]][0])
        ind = index[0]

    temp_array = data_array[ind][user_selection]
    data_array[ind][user_selection] = data_array[ind][user_selection].replace(old_item, new_item, 1).strip()

    if data_array[ind][user_selection] == temp_array:
        print(data_array[ind])
        print('Обновление записи не произошло.\nПроверьте правильность введённых данных.')
    else:
        write_file(flname, data_array)
        if user_selection == 1:
            print(f'Успешно изменена фамилия с {old_item} на {new_item} в записи с ID {id}')
        elif user_selection == 2:
            print(f'Успешно изменено имя с {old_item} на {new_item} в записи с ID {id}')
        elif user_selection == 3:
            print(f'Успешно изменено отчество с {old_item} на {new_item} в записи с ID {id}')
        elif user_selection == 4:
            print(f'Успешно изменён номер телефона с {old_item} на {new_item} в записи с ID {id}')
        print(data_array[ind])


def delete_record(flname, index):
    data = read_file(flname)

    if len(index) > 1:
        ind, id = list_records(data, index)
        print(data[ind])
    else:
        print('Найдена запись:')
        print(data[index[0]])
        id = data[index[0]][0]

    print('Удалить найденную запись? y/n')
    resp = input()
    if resp == 'n' or resp == 'N':
        print('Повторите выбор')
        menu()
    else:
        with open(flname, "r+") as file:
            data_array = file.readlines()
            file.seek(0)
            for i in range(len(data_array)):
                if i != index[0]:
                    file.write(data_array[i])
            file.truncate()
        print(f'Запись c ID {id} успешно удалена')


def select_menu(flname, opt=''):
    print('Ищем запись по ID? y/n')
    user_selection = input()
    if user_selection == 'y' or user_selection == 'Y':
        id = input('Введите ID записи: ')
        user_selection = 0
        res, index = search_for_record(flname, user_selection, id)
        if res == True:
            if opt == 'delete':
                delete_record(flname, index)
            else:
                update_menu(index)
    elif user_selection == 'n' or user_selection == 'N':
        index = [0]
        update_menu(index, opt)


def update_menu(ind=None, opt=''):
    if ind is None:
        ind = [0]
    if opt == 'delete':
        print('Ищем: ')
    else:
        print('Изменяем:')
    print('1 - Фамилию')
    print('2 - Имя')
    print('3 - Отчествo')
    print('4 - Номер телефона')
    user_selection = int(input())
    old_item = new_item = ''
    if user_selection == 1:
        old_item = input('Введите фамилию: ')
        if opt == '':
            new_item = input('Введите новую фамилию: ')
    elif user_selection == 2:
        old_item = input('Введите имя: ')
        if opt == '':
            new_item = input('Введите новое имя: ')
    elif user_selection == 3:
        old_item = input('Введите отчество: ')
        if opt == '':
            new_item = input('Введите новое отчество: ')
    elif user_selection == 4:
        old_item = input('Введите номер телефона: ')
        if opt == '':
            new_item = input('Введите новый номер телефона: ')

    if ind[0] > 0:
        update_record(flname, ind, old_item, new_item, user_selection)
    else:
        res, index = search_for_record(flname, user_selection, old_item)
        if res == True:
            if opt == 'delete':
                delete_record(flname, index)
            else:
                update_record(flname, index, old_item, new_item, user_selection)


def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(flname)
    elif user_operation == 2:
        add_item(flname)
    elif user_operation == 3:
        select_menu(flname)
    elif user_operation == 4:
        select_menu(flname, 'delete')


flname = 'phone_book.txt'
menu()
