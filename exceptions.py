import os


class MyError(Exception):
    pass

def empty_value(value):
    if value == '':
        raise MyError('Поле не может быть пустым')
    else:
        return value

def correct_stores_list(stores_list):
    '''Проверяем, что список торговых точек не пуст и в нем нет повторяющихся значений'''

    stores_list = stores_list.strip().split('\n')

    if len(stores_list) == 1 and stores_list[0] == '':
        raise MyError('список не может быть пустым')
    else:
        if any([row == '' for row in stores_list]):
            raise MyError('в списке не может быть пустых строк')
        else:
            if len(stores_list) != len(set(stores_list)):
                raise MyError('в списке есть повторяющиеся значения')
            else:
                return stores_list

def correct_api(api_key):
    '''Проверяем, что поле не пустое'''

    if api_key == '':
        raise MyError('поле не может быть пустым')
    else:
        return api_key

def correct_brand(brand_name):
    '''Проверяем, что папка с таким названием бренда - уникальна и поле не пустое'''

    if brand_name == '':
        raise MyError('поле не может быть пустым')
    elif os.path.isdir(f'{brand_name}'):
        raise MyError('папка бренда с таким названием уже существует')
    else:
        return brand_name


def correct_shop_code(code: str) -> int:
    '''Обрабатываем значение введенное в поле Начальный код точек
    Если значение текст или меньше 1, возбуждаем исключение
    Если значение - целое число больше 0, то возвращаем его'''

    try:
        code = int(code)
    except:
        raise MyError('значение должно быть целым числом больше 0')
    else:
        if code < 1:
            raise MyError('значение должно быть целым числом больше 0')
        else:
            return code