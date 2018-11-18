'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''

# Размер списка рандомный от 5 до 10 элементов

import random

def sorting(list_):
    def result(left, right):
        i = 0
        j = 0
        answer = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                answer.append(left[i])
                i += 1
            else:
                answer.append(right[j])
                j += 1
        answer += left[i:]
        answer += right[j:]
        return answer

    if len(list_) < 2:
        return list_
    middle = len(list_) // 2
    left = sorting(list_[:middle])
    right = sorting(list_[middle:])
    return result(left, right)

LIST_VALUES = [0, 49]
LIST_RANGE = [5, 10]

list_ = [random.randint(*LIST_VALUES) + random.random() for i in range(random.randint(*LIST_RANGE))]

print('Несортированный список:', list_)
print('Отсортированный список:', sorting(list_))


