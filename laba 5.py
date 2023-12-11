"""Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу
сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и
итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и
графической форме в виде отчета по лабораторной работе.

Вариант 7:
F(1) = 19
F(n) = -(3*F(n–1) – 2*F(n–2))
при n >=2"""

import time
import matplotlib.pyplot as plt
import sys

if hasattr(sys, "set_int_max_str_digits"):
    upper_bound = 0
    lower_bound = 4004
    current_limit = sys.get_int_max_str_digits()
    if current_limit == 0 or current_limit > upper_bound:
        sys.set_int_max_str_digits(upper_bound)
    elif current_limit < lower_bound:
        sys.set_int_max_str_digits(lower_bound)
        
def rec_f(n):
    if n <= 1:
        return 19
    elif n >= 2:
        return -(3 * rec_f(n - 1) - 2 * rec_f(n - 2))


def iter_f(n):
    fn = [19] * 3
    for _ in range(2, n+1):
        fn[-1] = -(3 * fn[-2] - 2 * fn[-3])
        fn[0], fn[1] = fn[1], fn[2]
    return fn[-1]


try:
    k = 1

    n = int(input('Введите натуральное число n, для функции: F(1) = 19; F(n) = -(3*F(n–1) – 2*F(n–2)): '))
    while n < 1:
        n = int(input('Введите число n больше 0. Рассматривается только последовательность натуральных чисел: '))

    o = int(input('\nДля какой функции вы хотите выполнить программу? '
                  '( Итерационной = 0 | Рекурсивной = 1 | Для обеих = 2 ): '))
    while o != 0 and o != 1 and o != 2:
        o = int(input('\nПринимаются только значения "0", "1" или "2": '))

    try:
        s = int(input('\nВведите натуральное число s, являющееся шагом в сравнительной таблице и графике: '))
    except ValueError:
        s = 1

    rec_times = []
    rec_values = []
    iter_times = []
    iter_values = []
    n_values = list(range(1, n + 1, s))

    if o == 0:
        if n > 90000:
            k = int(input('\nЧисло n слишком большое. Работа программы может занять существенное время.'
                          ' Хотите получить результат? ( Да = 1 | Нет = 0 ): '))
        while k != 0 and k != 1:
            k = int(input('\nПринимаются только значения "1" или "0": '))

        if k == 1:
            start = time.time()
            result = iter_f(n)
            end = time.time()
            print(f'\nРезультат (итерация): {result}\nВремя выполнения (итерация): {end - start} cек.')

            for n in n_values:
                start = time.time()
                iter_values.append(iter_f(n))
                end = time.time()
                iter_times.append(end - start)

            plt.plot(n_values, iter_times, label='Итерационная функция.')
            plt.legend(loc=2)
            plt.xlabel('Значение n')
            plt.ylabel('Время выполнения (c)')
            plt.show()
        else:
            print('\nРабота программы завершена.')
            quit()

    elif o == 1:
        if n > 32:
            k = int(input('\nЧисло n слишком большое. Работа программы может занять существенное время.'
                          ' Хотите получить результат? ( Да = 1 | Нет = 0 ): '))
        while k != 0 and k != 1:
            k = int(input('\nПринимаются только значения "1" или "0": '))

        if k == 1:
            start = time.time()
            result = rec_f(n)
            end = time.time()
            print(f'\nРезультат (рекурсия): {result}\nВремя выполнения (рекурсия): {end - start} cек.')

            for n in n_values:
                start = time.time()
                rec_values.append(rec_f(n))
                end = time.time()
                rec_times.append(end - start)

            # Вывод графика
            plt.plot(n_values, rec_times, label='Рекурсивная функция.')
            plt.legend(loc=2)
            plt.xlabel('Значение n')
            plt.ylabel('Время выполнения (c)')
            plt.show()
        else:
            print('\nРабота программы завершена.')
            quit()

    elif o == 2:
        # Проверка на ожидание
        if n > 32:
            k = int(input(
                '\nЧисло n слишком большое. Работа программы может занять существенное время.'
                ' Хотите получить результат? ( Да = 1 | Нет = 0 ): '))
        while k != 0 and k != 1:
            k = int(input('\nПринимаются только значения "1" или "0": '))

        if k == 1:
            # Итерационный подход
            start = time.time()
            result = iter_f(n)
            end = time.time()
            print(f'\nРезультат: {result}\nВремя выполнения (итерация): {end - start} cек.')
            # Рекурсивный подход
            start = time.time()
            result = rec_f(n)
            end = time.time()
            print(f'Время выполнения (рекурсия): {end - start} cек.')

            for n in n_values:
                start = time.time()
                rec_values.append(rec_f(n))
                end = time.time()
                rec_times.append(end - start)

                start = time.time()
                iter_values.append(iter_f(n))
                end = time.time()
                iter_times.append(end - start)

            table = []

            for i, n in enumerate(n_values):
                table.append([n, iter_values[i], rec_values[i], iter_times[i], rec_times[i]])
            # Вывод таблицы
            a = '¯' * 112
            b = '_' * 112
            c = '-' * 112
            print('\nТаблица:')
            print(f'|{a}|')
            print('|{:^4}|{:^26}|{:^26}|{:^26}|{:^26}|'.format('n', 'Значение итерации', 'Значение рекурсии',
                                                               'Время итерации(с)', 'Время рекурсии(с)'))
            print(f'|{c}|')
            for value in table:
                print('|{:^4}|{:^26}|{:^26}|{:^26}|{:^26}|'.format(value[0], value[1], value[2], value[3], value[4]))
            print(f'|{b}|')

            print('\nОтчёт:\nУже при n > 32 время работы рекурсивной функции начинает превышать секунду.\nА предел'
                  ' глубины рекурсии наступает на 1 000. Тем временем итерационный подход справляется за меньше чем'
                  ' секунду при значениях n > 95 000.\nИ ограничен лишь временем. Поэтому итерационный подход'
                  ' эффективен как по времени работы, так и по пределу вводимых значений.')
            # Вывод графика
            plt.plot(n_values, rec_times, label='Рекурсивная функция.')
            plt.plot(n_values, iter_times, label='Итерационная функция.')
            plt.legend(loc=2)
            plt.xlabel('Значение n')
            plt.ylabel('Время выполнения (c)')
            plt.show()
        else:
            print('\nРабота программы завершена.')
            quit()

    print('\nРабота программы завершена.')
    
except ValueError:
    print(f'Перезапустите программу и введите число, а не символ.')
except RecursionError:
    print(
        '\nВы превысили относительную максимальную глубину рекурсии. Перезапустите программу и введите число меньше.')

