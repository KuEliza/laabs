"""
Вариант 7.
Четные восьмиричные числа, не превышающие 2048, у которых вторая справа цифра равна 0. Выводит на экран цифры, до этого 0.
Вычисляется среднее число между минимальным и максимальным и выводится прописью.
"""

import re

m = []


def slovo(x):
    z = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь',
         '8': 'восемь', '9': 'девять'}
    return z[x]


f = open('test.txt')
buf = f.readline().split()
if not buf:
    print('Файл пустой.')
    quit()
else:
    while True:
        if not buf:
            break
        for i in buf:
            wb = re.findall(r'[0-7]*0[0246]', i)
            if wb:
                if int(wb[0]) < 4001 and len(wb[0]) == len(i):
                    m += [int(wb[0])]
                    l = wb[0][:-2]
                    print(f'Вывод: {l}')
        buf = f.readline().split()

if m:
    sred = (max(m) + min(m)) // 2
    k = ''
    for i in range(len(str(sred))):
        g = slovo(str(sred)[i])
        k += g + ' '
    print(f'Среднее значение: {sred} - {k}')
else:
    print('В файле нет подходящих значений.')
