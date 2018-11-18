'''
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
'''

#Размер списка рандомный от 11 до 21 с шагом 2

import random

LIST_VALUES = [-10, 10]
LIST_RANGE = [5, 10]

list_ = [random.randint(*LIST_VALUES) for _ in range(2 * random.randint(*LIST_RANGE) + 1)]
print('Список:', list_)

for n in range(len(list_)):
    c = list_.count(list_[n])
    menshe = 0
    bolshe = 0
    for i in range(len(list_)):
        if list_[i] >= list_[n]:
            bolshe += 1
        if list_[i] <= list_[n]:
            menshe += 1

    if abs(bolshe - menshe) < c:
        print('Медиана:', list_[n])
        #print('Проверка:')
        #list2 = sorted(list_)
        #print(list2[:len(list_) // 2], list2[len(list_) // 2], list2[len(list_) // 2 + 1:])
        break



