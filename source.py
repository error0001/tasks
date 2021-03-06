# tasks https://pythonworld.ru/osnovy/tasks.html
import unittest


def arithmetic_(in_a, inB, inOper):
    if isinstance(in_a,str):
        in_a = float(in_a)
    if isinstance(inB,str):
        inB = float(inB)
    if in_a != None and inOper != None and inB != None:
        if inOper == '+':
            return in_a + inB
        if inOper == '-':
            return in_a - inB
        if inOper == '*':
            return in_a * inB
        if inOper == '/' and in_a != 0 and inB != 0:
            return float(in_a / inB)

# https://www.w3resource.com/python-exercises/list/
# tasks about list


'''#class is example, how you will check your feature
class ArithmeticTestCase(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(arithmetic_(3,4,'+'), 7)
    def test_minus(self):
        self.assertEqual(arithmetic_(3,4,'-'), -1)
    def test_multi(self):
        self.assertEqual(arithmetic_(3,4,'*'), 12)
    def test_divide(self):
        self.assertEqual(arithmetic_(3,4,'/'), 3/4)
    #def test_unknow(self):
     #   self.assertEqual(Arithmetic(3,4,'.'), "the unknow operation")

'''


def merge_two_dicts(in_dict0, in_dict1):
    """
    слиянеие двух словарей для функции _account_tax_first_level, смотреть файл report
    :param in_dict0: первый словарь
    :param in_dict1: второй словарь
    :return: возвращает объединенный словарь
    """
    # merged_dict = in_dict0.copy()   # делаем копию правой части, чтобы случайно не изменить вх. dict
    result_dict = {}
    if isinstance(in_dict0, dict) and isinstance(in_dict1, dict):
        result_dict = in_dict0.copy()
        result_dict.update(in_dict1)    # производим сляние dict'ов

    return result_dict


def sum_list_(in_list):
    """
    Function is calculating as sum all elements of list.
    :param in_list: incoming iterator of list
    :return:
    """
    # realize of protection: test type and test len
    if isinstance(in_list, list) and len(in_list) != 0:
        print('ok list in work...')
        flag_float = False
        some_sum = 0
        # !еще сделать защиту от пустого листа
        # condition for slicing(среза) point of float, after iteration
        if isinstance(in_list[0], bool):
            print("We have problem with type of set object")
            return 0
        if isinstance(in_list[0], float):
            flag_float = True
        # iteration
        for xl in in_list:   # 0, len(in_list)):
            some_sum = some_sum + xl
        # slicing(срез) point if elements in the list is float type
        if flag_float is True:
            return round(some_sum, 3)
        else:
            return some_sum
    else:
        print("We have problem with type of set object")
        return 0


def multiply_all_list(in_list):
    """
    la la land
    :param in_list: la la land
    :return: value not list, tuple or dict
    """
    if isinstance(in_list, list) and len(in_list) != 0:
        answer = 1
        error_count = 0
        # protection without bool type
        for x in in_list:
            if isinstance(x, (int, float)) and x is not None:
                answer = answer * x
            else:
                error_count = error_count + 1
        print("Error count in list is: ", error_count)
        return answer
    print("Type not correct")
    return 0


# task 3
def get_list_max(in_list):
    """

    :param in_list:
    :return:
    """
    if isinstance(in_list, list) and len(in_list) != 0 and in_list is not None:
        temp_list = []  # temporary list
        error_count = 0
        # protection without bool type
        for x in in_list:
            if isinstance(x, (int, float)) and x is not None:
                temp_list.append(x)
            else:
                error_count = error_count + 1
        print("Error count in list is: ", error_count)
        print(temp_list)
        del error_count   # delete trash
        return max(temp_list)
    print("Type not correct")
    return 0


# task 4
def get_min_at_list(in_list):
    """
    la la land
    :param in_list: la la land
    :return: min of list
    """
    if isinstance(in_list, list) and len(in_list) != 0 and in_list is not None:
        temp_list = []  # temporary list
        error_count = 0
        for x in in_list:
            if isinstance(x, (int, float)):
                temp_list.append(x)
            else:
                error_count += 1
        print("Errors of elements: ", error_count)
        print(temp_list)
        min_val = min(temp_list)    # нафиг его хранить в памяти?
        del error_count
        del temp_list
        return min_val

    return 0


# task 5
''' Write a Python program 
    to count the number of strings where the string length is 2 or more 
    and the first and last character are same from a given list of strings.
     
    Фнукция ищет индекс слова, в котором первая и последние символы равны.
    После анализа возвращает, индекс слова.
     
    def get_clone_char(in_list):
    
    Sample List : ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2
'''


def get_clone_char(in_list, key):
    """
    la la bla
    :param in_list: la la bla
    :param key: la la la
    :return: index
    """
    if key is None:
        key = 's'

    if isinstance(in_list, list) and len(in_list) is not 0 and in_list is not None:
        index_cnt = 0
        error_count = 0
        error_type_cnt = 0
        # перебрали лист на данные
        for x in in_list:
            # проверили ключ на какие данные ссылаем s is str
            if key is 's':
                if isinstance(x, str):
                    # логика
                    # проверка на длину слова и значение первого с последним
                    if len(x) > 1 and x[0] == x[-1]:
                        index_cnt += 1
                else:
                    error_count += 1
            else:
                error_type_cnt += 1
        return index_cnt
    return 0


# task 6
''' Write a Python program
    to get a list, sorted in increasing order 
    by the last element in each tuple from a 
    given list of non-empty tuples.
    ///  
    Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
    ///
    Did:
        list of tuples ex: [(...),...]
'''


def sort_elements_in_lists(in_list):
    """
    функция сортировки второго уровня
    :param in_list: [(x7,3),(x1,2)..]
    :return: зипованный и отсортированный лист
    """
    if isinstance(in_list, list):
        # сначала вытащим растегнем zip
        ls1, ls2 = zip(*in_list)
        # отсортируем второй массив
        ls2 = sorted(ls2)
        # сделаем обратно zip
        # out :[(x7, 2), (x1, 3)..]
        result = list(zip(ls1, ls2))
        return result
    ''' for main
        test_list = [(45, 2), (41, 1), (412,7), (132, 3), (14, 10), (411, 122), (34, 20), (12, 4)]
        print(test_list)
        result = sort_elements_in_lists(test_list)
        print(result)
    '''
    return 0

# task 7
# Write method which delete duplicate in list


def delete_duplicate(in_list):
    """
    удаляет дублированные значения в списке
    :param in_list:
    :return: возвращает подчищенный лист
    """
    # КОШМАРНЫЙ ВАРИАНТ МОЕГО ВОСПОЛЕННОГО ВООБРАЖЕНИЯ, но работает
    tmp_list = in_list.copy()
    count = 0
    count_list = []
    if isinstance(tmp_list, list):
        for x in tmp_list:
            count += 1
            if count != len(tmp_list):
                if x == tmp_list[count]:
                    count_list.append(tmp_list[count])
        print("Duplicate indexes: ", count_list)
        for x in count_list:
            tmp_list.remove(x)
        del count
        del count_list
        return tmp_list
    '''
        ls = [3, 1, 3, 54, 66, 3, 1, 4, 7, 30, 1]
        ls = sorted(ls)
        print(ls)
        print(delete_duplicate(ls))
    '''
    return 0


def delete_duplicate_(in_list):
    # вариант решения с сайта
    dup_items = set()
    uniq_items = []
    for x in in_list:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    return dup_items


# task 10
''' Write a Python program 
    to find the list of 
    words that are longer 
    than n from a given 
    list of words.
'''


def find_max_words(sentense, max_word):
    """
    функция ищет самые длинные предложения
    example:
        ls = "asf fefewv edweef dccs qdwqdwed."
        print(find_max_words(ls, 4))
    :param sentense: предложение
    :param max_word: максимальная длина слова
    :return:
    """
    # разобьем предложения на слова и засунем в лист
    tmp_list = sentense.split()
    result_list = []
    # после разобьем все слова и переопределим, так
    # чтобы буквы были в каждом листе и считаем
    for item in tmp_list:
        if len(list(item)) >= max_word:
            result_list.append(item)
    return result_list

# task 11
''' Write a Python function 
that takes two lists 
and returns True if they have at least one common member
'''


def find_common(list0, list1):
    """
        ls0 = range(10)
        ls1 = range(10, 15)
        print(find_common(ls0, ls1))
    :param list0:
    :param list1:
    :return:
    """
    for item in list0:
        if item in list1:
            return True
    return False


# task 12
'''Write a Python program to print 
a specified list after 
removing the 0th, 4th and 5th 
elements. 
Example:
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''

def func_del_other(in_list):
    print(in_list)
    for item in in_list:
        print(item)
        if len(item) >= 5:
            in_list.remove(item)
    return in_list


''' Task 20 
написать программу которая
находит разницу в двух листах
'''


def get_diff_list(in_left, in_right):
    if isinstance(in_left, list) and isinstance(in_right, list):
        return list(set(in_left) - set(in_right))
    return 0


''' Task 21
конвертирует все список символов в строку
'''


# def chrs_to_str(in_list):
#     if isinstance(in_list, list):
#         temp_row = ""
#         for x in in_list:
#             if isinstance(x, chr)
#                 temp_row += x
#         return temp_row
#     return 0


from collections import ChainMap

car_parts = {
    'hood': 500,
    'engine': 5000,
    'front_door': 750
}

car_options = {
    'A/C': 1000,
    'Turbo': 2500,
    'rollbar': 300
}

car_accessories = {
    'cover': 100,
    'hood_ornament': 150,
    'seat_cover': 99
}


import itertools


def stud_sets(s, counter=20):
    students = set(s)
    subset4 = itertools.combinations(students, 4)
    for c4 in subset4:
        subset3 = itertools.combinations(students - set(c4), 3)
        for c3 in subset3:
            subset1 = itertools.combinations(students - set(c4) - set(c3), 1)
            for c1 in subset1:
                print(c4, " + ", c3, " + ", c1)
                counter -= 1
                if counter == 0:
                    return None


"""
Создайте словарь, связав его с переменной school, и 
наполните данными, которые бы отражали количество учащихся в 
разных классах (1а, 1б, 2б, 6а, 7в и т. п.). 
Внесите изменения в словарь согласно следующему: 
а) в одном из классов изменилось количество учащихся, 
б) в школе появился новый класс, 
с) в школе был расформирован (удален) другой класс. 
Вычислите общее количество учащихся в школе.
"""
def task0():
    school = dict()
    # исп. итератор
    # '1a': [family, year]
    # 1 добавляет к строчке цифру, и несколько букв(5 букв), инкремент класса


# курс 9
# задача 1
# + Реализовать две функции:
# write_to_file(data)
# read_file_data().
# Которые соотвественно: пишут данные в
# файл и читают данные из файла.
# def write_to_file(data):
#     with open(data, mode=mode) as some_data:
#         return some_data
from urllib import request, response
import urllib
import urllib3
import json
# популярный модуль, для запросов, так как упрощает множество строчек кода
import requests

def get_habr():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://habrahabr.ru/')
    print('******************')
    print(r.status)
    print('******************')
    print(r.data)
    print('******************')
    print(r.headers)


if __name__ == '__main__':
    try:
        print("*Start********")
        get_habr()
    except urllib3.exceptions.MaxRetryError as ert:
        print('Error: ', ert)
    finally:
        print("End")

