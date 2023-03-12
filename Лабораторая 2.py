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
buffer = f.readline().split()
if not buffer:
    print('Файл пустой.')
    quit()
else:
    while True:
        if not buffer:
            break
        for i in buffer:
            work_buffer = re.findall(r'[0-7]*0[0246]', i) #re.findall(pattern, string)
                                                        #Найти в строке string все непересекающиеся шаблоны pattern;
            if work_buffer:
                if int(work_buffer[0]) < 4001 and len(work_buffer[0]) == len(i):
                    m += [int(work_buffer[0])]
                    l = work_buffer[0][:-2]
                    print(f'Вывод: {l}')
        buffer = f.readline().split()

if m:
    sred = (max(m) + min(m)) // 2
    k = ''
    for i in range(len(str(sred))):
        g = slovo(str(sred)[i])
        k += g + ' '
    print(f'Среднее значение: {sred} - {k}')
else:
    print('В файле нет подходящих значений.')