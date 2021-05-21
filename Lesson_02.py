# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа
# данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не
# запрашивать у пользователя, а указать явно, в программе.
print('-----------------Задание 1-----------------------')
my_int = 12
my_float = 2.4
my_str = "Lesson_02"
my_list = ['a', 'b', 'c', 1, 2]
my_tuple = ('a', 'b', 'c', 1, 2)
my_dict = {'name': 'Иван', 'Last': 'Петров'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')
print('-------------------------------------------------')




# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
print('-----------------Задание 2-----------------------')

my_lists = ['1', '2', '3', '4', '5']
if len(my_lists) % 2 == 0:
    i = 0
    while i < len(my_lists):
        el = my_lists[i]
        my_lists[i] = my_lists[i+1]
        my_lists[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_lists) - 1:
        el = my_lists[i]
        my_lists[i] = my_lists[i + 1]
        my_lists[i + 1] = el
        i += 2
print(my_lists)
print('-------------------------------------------------')



# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
print('-----------------Задание 3-----------------------')

number = int(input("Введите номер месяца: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'Январь',
                  2: 'Февраль',
                  3: 'Март',
                  4: 'Апрель',
                  5: 'Май',
                  6: 'Июнь',
                  7: 'Июль',
                  8: 'Август',
                  9: 'Сентябрь',
                  10: 'Октябрь',
                  11: 'Ноябрь',
                  12: 'Декабрь'}
    season_dict = {1: 'Зима',
                  2: 'Зима',
                  3: 'Весна',
                  4: 'Весна',
                  5: 'Весна',
                  6: 'Лето',
                  7: 'Лето',
                  8: 'Лето',
                  9: 'Осень',
                  10: 'Осень',
                  11: 'Осень',
                  12: 'Зима'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number - 1:
            print(f"Месяц {el}")
    season_list = list(season_dict.values())
    for l, ele in enumerate(season_list):
         if l == number - 1:
            print(f"Сезон {ele}")
            break
else:
    print("Ввели не верное значение. У нас всего 12 месяцев :)))")
print('-------------------------------------------------')



# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с
# новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
print('-----------------Задание 4-----------------------')
my_str = input("Введите строку из слов: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")
print('-------------------------------------------------')



# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
print('-----------------Задание 5-----------------------')
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (111 - выход) "))
while digit != 111:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))
print('-------------------------------------------------')



# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

print('-----------------Задание 6-----------------------')
# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
# товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

goods = []
while input("Желайте добавить продукт? Введите yes/no: ") == 'yes':
    number = int(input("Введите номер продукта: "))
    features = {}
    while input("Желайте досбавить параметры продукта? Введите yes/no: ") == 'yes':
        feature_key = input("Введите название: ")
        feature_value = input("Введите количество: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
#goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)