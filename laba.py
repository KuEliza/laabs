"""Вариант 7.
Четные восьмиричные числа, не превышающие 2048, у которых вторая справа цифра равна 0. Выводит на экран цифры, до этого 0.
Вычисляется среднее число между минимальным и максимальным и выводится прописью."""
n = []
znak = [' ', '!', '?', '.', ',', '\n', '']
chisl = ['0', '1', '2', '3', '4', '5', '6', '7']
bl = 1
wb = ''

def byk(x):
    a = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
         '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
         }
    return a[x]

with open('test.txt') as f:
    bb = f.read(bl)
    if not bb:
        print('Файл пуст.')
        quit()
    while bb: 
        while bb not in znak:
            wb += bb
            bb = f.read(bl)
        if len(wb) > 0:
            prav = True
            for i in range(len(wb)):
                if wb[i] not in chisl:
                    prav = False
                    break
            if prav and len(wb) > 2:
                if wb[0] != '0' and wb[-2] == '0' and int(wb) < int(oct(2049)[2::]) and int(wb) % 2 == 0:
                    n += [int(wb)]
                    l = wb[:-2:]
                    print(f'Вывод: {l}')
        wb = ''
        bb = f.read(bl)
if n: 
    sz = (max(n) + min(n)) // 2
    k = ''
    for i in range(len(str(sz))):
        g = byk(str(sz)[i])
        k += g + ' '
    print(f'Среднее значение: {sz} - {k}.')
else:
    print('В файле нет подходящих значений.')

