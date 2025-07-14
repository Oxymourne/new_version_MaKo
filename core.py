import os
import shutil

from exceptions import MyError


def auto_main_function(magazines_list, api_key, brand_name, port, start_code, check_sms, plugin_version):
    '''Основная функция для автоматической версии, которая:
        1. Создает папку с названием бренда
        2. В этой папке создает папки с названиеми торговых точек
        3. В папку копирует плагин из папки "Донор"
        4. Запускает функцию config_changer, чтобы изменить конфиг
        '''

    def config_changer():
        '''Второстепенная функция, которая:
        1. Открывает файл конфига
        2. Находит нужные строки
        3. Вставляет пользовательские значения
        '''

        with open(
                f'{brand_name}/{magazine}/{plugin_version}/Resto.Front.Api.CloudLoyalty.dll.config',
                'r', encoding='utf-8') as infile:
            a = infile.readlines()
            res_list = []

            for i in a:
                if 'X-Processing-Key' in i:
                    b = i.split('X-Processing-Key')
                    i = f'{api_key}'.join(b)
                if 'Код торговой точки' in i:
                    b = i.split('Код торговой точки')
                    i = f'{start_code}'.join(b)
                if 'Название торговой точки' in i:
                    b = i.split('Название торговой точки')
                    i = f'{magazine}'.join(b)
                if 'send_sms' in i:
                    row_index = a.index(i) + 1
                    b = a[row_index].split('False')
                    a[row_index] = f'{check_sms}'.join(b)
                if 'server_port' in i:
                    if port != '':
                        row_index = a.index(i) + 1
                        b = a[row_index].split('0')
                        a[row_index] = f'{port}'.join(b)

                res_list.append(i)

            with open(
                    f'{brand_name}/{magazine}/{plugin_version}/Resto.Front.Api.CloudLoyalty.dll.config',
                    'w', encoding='utf-8') as infile:
                infile.writelines(res_list)

    os.mkdir(brand_name)
    stores_codes_list = []

    for magazine in magazines_list:
        shutil.copytree('Донор', f'{brand_name}/{magazine}')
        config_changer()
        stores_codes_list.append((magazine, start_code))
        start_code += 1

    with open(f'{brand_name}/Названия и коды точек.txt', 'w', encoding='utf-8') as code_file:
        max_len = len(max(stores_codes_list, key=lambda x: len(x[0]))[0])
        column_1 = 'Название точки'

        if max_len < len(column_1):
            max_len = len(column_1)

        column_2 = 'Код точки'
        code_file.write(f'{column_1}:{' ' * (max_len - len(column_1) + 1)}  {column_2}:\n')
        for row in stores_codes_list:
            code_file.write(f'{row[0]}{' ' * (max_len - len(row[0]) + 1)} | {row[1]}\n')


def custom_main_function(magazines_list, api_key, brand_name, port, codes_list, check_sms, plugin_version):
    '''Основная функция для кастомной версии, которая:
        1. Создает папку с названием бренда
        2. В этой папке создает папки с названиеми торговых точек
        3. В папку копирует плагин из папки "Донор"
        4. Запускает функцию config_changer, чтобы изменить конфиг
        '''

    def config_changer():
        '''Второстепенная функция, которая:
        1. Открывает файл конфига
        2. Находит нужные строки
        3. Вставляет пользовательские значения
        '''

        with open(
                f'{brand_name}/{magazine_code[0]}/{plugin_version}/Resto.Front.Api.CloudLoyalty.dll.config',
                'r', encoding='utf-8') as infile:
            a = infile.readlines()
            res_list = []

            for i in a:
                if 'X-Processing-Key' in i:
                    b = i.split('X-Processing-Key')
                    i = f'{api_key}'.join(b)
                if 'Код торговой точки' in i:
                    b = i.split('Код торговой точки')
                    i = f'{magazine_code[1]}'.join(b)
                if 'Название торговой точки' in i:
                    b = i.split('Название торговой точки')
                    i = f'{magazine_code[0]}'.join(b)
                if 'send_sms' in i:
                    row_index = a.index(i) + 1
                    b = a[row_index].split('False')
                    a[row_index] = f'{check_sms}'.join(b)
                if 'server_port' in i:
                    if port != '':
                        row_index = a.index(i) + 1
                        b = a[row_index].split('0')
                        a[row_index] = f'{port}'.join(b)

                res_list.append(i)

            with open(
                    f'{brand_name}/{magazine_code[0]}/{plugin_version}/Resto.Front.Api.CloudLoyalty.dll.config',
                    'w', encoding='utf-8') as infile:
                infile.writelines(res_list)

    os.mkdir(brand_name)
    stores_codes_list = []

    for magazine_code in list(zip(magazines_list, codes_list)):
        shutil.copytree('Донор', f'{brand_name}/{magazine_code[0]}')
        config_changer()
        stores_codes_list.append(magazine_code)

    with open(f'{brand_name}/Названия и коды точек.txt', 'w', encoding='utf-8') as code_file:
        max_len = len(max(stores_codes_list, key=lambda x: len(x[0]))[0])
        column_1 = 'Название точки'

        if max_len < len(column_1):
            max_len = len(column_1)

        column_2 = 'Код точки'
        code_file.write(f'{column_1}:{' ' * (max_len - len(column_1) + 1)}  {column_2}:\n')
        for row in stores_codes_list:
            code_file.write(f'{row[0]}{' ' * (max_len - len(row[0]) + 1)} | {row[1]}\n')


def plugin_name():
    name = os.listdir('Донор')
    if len(name) == 0:
        raise MyError('В папке Донор нет плагина')
    elif len(name) > 1:
        raise MyError('В папке Донор есть лишние папки')
    else:
        return name[0]
