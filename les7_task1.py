'''
1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Вывести на экран исходный и отсортированный массивы.
'''

# Размер списка рандомный от 10 до 20 элементов

import random

def sorting(spisok):
    for _ in range(len(spisok)):
        for i in range(1, len(spisok)):
            if spisok[i] > spisok[i - 1]:
                spisok[i], spisok[i - 1] = spisok[i - 1], spisok[i]
    return spisok


LIST_VALUES = [-100, 99]
LIST_RANGE = [10, 20]

list_ = [random.randint(*LIST_VALUES) for _ in range(random.randint(*LIST_RANGE))]
print('Несортированный список:', list_)
print('Отсортированный список:', sorting(list_))

