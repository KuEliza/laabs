"""
Лабораторная работа включает в себя два задания:
1) написать программу в соответствии со своим вариантом задания.
2) усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

Вариант 9:
Дана квадратная матрица. Сформировать все возможные варианты данной матрицы путём перестановки
элементов главной и побочной диагонали в каждой строке.
"""

import itertools
import copy
from random import *

matrix = []
summ = []
matrices = []


def gen_matrix(matrix):
    two_elem = []
    for row in range(len(matrix)):
        if row != len(matrix[row]) - 1 - row:
            two_elem.append([matrix[row][row], matrix[row][len(matrix) - 1 - row]])
            two_elem.append([matrix[row][len(matrix) - 1 - row], matrix[row][row]])
    return two_elem


def gen_matrix_even_row(matrix):
    two_elem = []
    for row in range(len(matrix)):
        if (row + 1) % 2 == 0 and row != len(matrix[row]) - 1 - row:
            two_elem.append([matrix[row][row], matrix[row][len(matrix) - 1 - row]])
            two_elem.append([matrix[row][len(matrix) - 1 - row], matrix[row][row]])
    return two_elem


def get_parameters(matrix):
    s = 0
    for i in range(len(matrix)):
        s += matrix[i][i]
    return s


try:
    a = int(input('Запустить обычную версию программы или усложнённую? ( Обычную = 0 | Усложнённую = 1 ): '))
    while a != 0 and a != 1:
        a = int(input('Принимаются только значения "0" и "1": '))

    n = int(input('\nВведите размерность матрицы: '))
    while n < 1:
        n = int(input('\nРазмерность матрицы должна быть больше ноля: '))

    matrix = [[randint(1, 9) for i in range(n)] for j in range(n)]

    # Первое задание
    if a == 0:
        m = copy.deepcopy(matrix)                     # копируем матрицу
        pairs = gen_matrix(m)                         # генерируем возможные пары каждой строки
        all_combs = list(itertools.permutations(pairs, len(m) - len(m) % 2))     # формируем всевозможные комбинаций пар элементов диагонали каждый строки
        combs = []  # список подходящих комбо
                                                    # проходимся по всем комбинациям
        for comb in all_combs:
            count = 0 
            for j in range(len(m) - len(m) % 2):                                 # центр матрицы для нечетных
                
                if comb[j] == pairs[j * 2] or comb[j] == pairs[(j * 2) + 1]:  
                    count += 1 
            if count == len(m) - len(m) % 2:  
                combs.append(comb)

        for comb in combs:
            new_matrix = copy.deepcopy(m)  # копируем матрицу
            k = 0  
            for j in range(len(new_matrix)):
                if j != len(new_matrix) - 1 - j:  # если мы не в центре в нечётной матрицы
                    new_matrix[j][j] = comb[k][0]
                    new_matrix[j][len(new_matrix) - 1 - j] = comb[k][1]
                    k += 1
            matrices.append(new_matrix)  

        print('\nМатрицы:')
        for i in range(len(matrices)):
            print('Матрица №' + str(i + 1))
            for row in matrices[i]:
                print("".join(['{:<4}'.format(item) for item in row]))
            print()

    # Второе задание
    else:
        print('\nДополнительным условием будет ограничение по перестановке только чётных строк.'
              '\nНужно вывести матрицы и их параметры и команду с наибольшей суммой элементов главной диагонали.')
        m = copy.deepcopy(matrix)  # копируем матрицу
        if len(m) < 4:  # если размер матрицы меньше 4, то в программе нет смысла
            print('\nМатрицы:')
            print('Матрица №1')
            for i in range(len(m)):
                print("".join(['{:<5}'.format(item) for item in m[i]]))
            print("Сумма элементов главной диагонали = " + str(get_parameters(m)) + '\n')
            print()
            exit()

        pairs = gen_matrix_even_row(m)  # генерируем возможные пары каждой строки
        all_combs = list(itertools.permutations(pairs, len(m) // 2 - len(m) // 2 % 2))  # формируем всевозможные комбинаций пар элементов диагонали каждой строки
        combs = []  # список подходящих комбо

        # проходимся по всем комбинациям
        for comb in all_combs:
            count = 0  
            for j in range(1, len(m), 2):  # проходимся по чётным строкам
                if comb[j // 2] == pairs[j // 2 * 2] or\
                        comb[j // 2] == pairs[j // 2 * 2 + 1]: 
                    count += 1 
            if count == len(m) // 2 - len(m) % 2:  
                combs.append(comb)

        for comb in combs:
            new_matrix = copy.deepcopy(m)  
            k = 0  
            for j in range(len(new_matrix)):
                if j != len(new_matrix) - 1 - j and (j + 1) % 2 == 0:  # если мы не в центре в нечётной матрицы
                    new_matrix[j][j] = comb[k][0]
                    new_matrix[j][len(new_matrix) - 1 - j] = comb[k][1]
                    k += 1
            matrices.append(new_matrix)  # добавим матрицу в список результатов

        print('\nМатрицы:')
        for i in range(len(matrices)):
            print('Матрица №' + str(i + 1))
            for row in matrices[i]:
                print("".join(['{:<5}'.format(item) for item in row]))
            summ.append(get_parameters(matrices[i]))
            print("Сумма элементов главной диагонали = " + str(summ[i]))
            print()

        # Вывод таблицы
        print('Матрица с наибольшей суммой элементов главной диагонали:')
        max_index = summ.index(max(summ))
        print('Матрица №' + str(max_index + 1))
        for row in matrices[max_index]:
            print("".join(['{:<5}'.format(item) for item in row]))
        print("Сумма элементов главной диагонали = " + str(summ[max_index]))

    print('\nРабота программы завершена успешно.')
except ValueError:
    print('\nВы ввели символ, а не число, перезапустите программу и введите нужное число.')
