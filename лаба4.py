""" С клавиатуры вводятся два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B, C, D, E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
заполнение, а целенаправленное.
Вид матрицы А:
D Е
С В
Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графика.
Программа должна использовать функции библиотек numpy  и mathplotlib
Вариант 7:
Формируется матрица F следующим образом: скопировать в нее "А" и если в "С" количество нулевых элементов
в нечетных столбцах больше, чем количество нулевых  элементов в четных столбцах, то поменять местами С и В симметрично,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего если определитель матрицы А
больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * FТ, иначе вычисляется выражение
(AТ +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А,
F и все матричные операции последовательно.
"""

from math import ceil
import random as r
import numpy as np
from matplotlib import pyplot as plt


def heatmap(data, row_labels, col_labels, ax, cbar_kw=None, **kwargs):  # аннотированная тепловая карта
    if cbar_kw is None:
        cbar_kw = {}
    im = ax.imshow(data, **kwargs)
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)
    return im, cbar


def annotate_heatmap(im, data=None, textcolors=("black", "white"), threshold=0):
    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()
    kw = dict(horizontalalignment="center", verticalalignment="center")
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(data[i, j] > threshold)])
            text = im.axes.text(j, i, data[i, j], **kw)
            texts.append(text)
    return texts


try:
    n = int(input('Введите число N больше 4: '))
    k = int(input('Введите число K: '))
    while n < 5:
        n = int(input('Введите число N больше 4: '))

    cnt_b2 = sum_ch4 = sum_det_F = 0
    middle_n = ceil(n / 2)                # Середина матрицы
    A = np.zeros((n, n))                  # Задаём матрицу A
    for i in range(n):
        for j in range(n):
            A[i][j] = r.randint(0, 3)
    AT = np.transpose(A)                  # Транспонированная матрица А
    det_A = np.linalg.det(A)              # Определитель матрицы А
    F = A.copy()                          # Задаём матрицу F
    FT = AT.copy()                        # Транспонированная F
    G = np.zeros((n, n))                  # Заготовка матрицы G

    print('\nМатрица А:')
    print(A)
    print('\nТранспонированная А:')
    print(AT)

    # Выделяем матрицы E C B
    if n % 2 == 1:
        E = [A[i][middle_n - 1:n] for i in range(middle_n)]
        C = [A[i][0:middle_n] for i in range(middle_n - 1, n)]
        B = [A[i][middle_n - 1:n] for i in range(middle_n - 1, n)]
    else:
        E = [A[i][middle_n:n] for i in range(0, middle_n)]
        C = [A[i][0:middle_n] for i in range(middle_n, n)]
        B = [A[i][middle_n:n] for i in range(middle_n, n)]
        

    cnt_b2 = 0
    
    for i in range(middle_n):  # Считаем количество нулевых элементов в нечетных столбцах в матрице C
        for j in range(middle_n):
            if (j + 1) % 2 == 1:
                if C[i][j] == 0:
                    cnt_b2 += 1
    sum_ch4 = 0

    for i in range(middle_n):  # Считаем количество нулевых  элементов в четных столбцах в матрице C
        for j in range(middle_n):
            if (j + 1) % 2 == 0:
                if C[i][j] == 0:
                    sum_ch4 += 1
    print (cnt_b2)
    print (sum_ch4)
                    

    if cnt_b2 > sum_ch4:
        print(f'\nВ матрице "С" количество нулевых элементов в нечетных столбцах ({cnt_b2})')
        print(f'больше чем количество нулевых  элементов в четных столбцах в матрице ({sum_ch4})')
        print('поэтому местами "С" и "В" симметрично:')
        C, B = B, C
        for i in range(middle_n):
            C[i] = C[i][::-1]  # Симметрично меняем значения в C
            B[i] = B[i][::-1]  # Симметрично меняем значения в B
        if n % 2 == 1:
            for i in range(middle_n - 1, n):  # Перезаписываем С
                for j in range(middle_n):
                    F[i][j] = C[i - (middle_n - 1)][j]
            for i in range(middle_n - 1, n):  # Перезаписываем B 
                for j in range(middle_n - 1, n):
                    F[i][j] = B[i - (middle_n - 1)][j - (middle_n - 1)]
        else:
            for i in range(middle_n, n):
                for j in range(middle_n):
                    F[i][j] = C[i - middle_n][j]
            for i in range(0, middle_n):
                for j in range(middle_n, n):
                    F[i][j] = B[i][j - middle_n]
    else:
        print(f'\nВ матрице "С" количество нулевых элементов в нечетных столбцах ({cnt_b2})')
        print(f'меньше количества нулевых  элементов в четных столбцах в матрице({sum_ch4}) или равно ему')
        print('поэтому несимметрично меняем местами подматрицы С и E:')
        C, E = E, C
        if n % 2 == 1:
            for i in range(middle_n - 1, n):        # Перезаписываем С
                for j in range(middle_n):
                    F[i][j] = C[i - (middle_n - 1)][j]
            for i in range(middle_n):               # Перезаписываем Е
                for j in range(middle_n - 1, n):
                    F[i][j] = E[i][j - (middle_n - 1)] 
        else:
            for i in range(middle_n, n):
                for j in range(middle_n):
                    F[i][j] = C[i - middle_n][j]  # Перезаписываем  C
            for i in range(0, middle_n):
                for j in range(middle_n, n):
                    F[i][j] = E[i][j - middle_n]  # Перезаписываем Е

    print('\nМатрица F:')
    print(F)
    # Сумма диагональных элементов матрицы F
    for i in range(n):
        for j in range(n):
            if i == j:
                sum_det_F += F[i][j]
            if (i + j + 1) == n and ((i == j) != ((i + j + 1) == n)):
                sum_det_F += F[i][j]

    if det_A > sum_det_F:
        print(f'\nОпределитель матрицы А({int(det_A)})')
        print(f'больше суммы диагональных элементов матрицы F({int(sum_det_F)})')
        print('поэтому вычисляем выражение: A * AT – K * FТ:')

        try:
            KFT = FT * k  # K * FT
            A_AT = np.matmul(A, AT)  # A * AT
            result = A_AT - KFT  # A * AT – K * FT

            print('\nРезультат K * FT:')
            print(KFT)
            print("\nРезультат A * AT:")
            print(A_AT)
            print('\nРезультат A * AT – K * FТ:')
            print(result)
        except np.linalg.LinAlgError:
            print("Одна из матриц является вырожденной (определитель равен 0),"
                  " поэтому обратную матрицу найти невозможно.")
    else:
        print(f'\nОпределитель матрицы А({int(det_A)})')
        print(f'меньше суммы диагональных элементов матрицы F({int(sum_det_F)}) или равен ей')
        print('поэтому вычисляем выражение (AТ + G - F - 1) * K:')

        for i in range(n):
            for j in range(n):
                if i >= j and (i + j + 1) >= n:
                    G[i][j] = A[i][j]

        ATG = AT + G  # AТ + G
        ATGFT = ATG - F  # AT + G - FT
        ATGFT_1 = ATGFT - 1 # AТ + G - F - 1
        result = ATGFT_1 * k  # (AТ + G - FТ) * K

        print('\nМатрица G:')
        print(G)
        print('\nРезультат AТ + G:')
        print(ATG)
        print('\nРезультат AТ + G - F:')
        print(ATGFT)
        print('\nРезультат AТ + G - F - 1:')
        print(ATGFT_1)
        print('\nРезультат (AТ + G - F - 1) * K:')
        print(result)

    av = [np.mean(abs(F[i::])) for i in range(n)]
    av = int(sum(av))  # сумма средних значений строк (используется при создании третьего графика)
    fig, axs = plt.subplots(2, 2, figsize=(11, 8))
    x = list(range(1, n + 1))
    for j in range(n):
        y = list(F[j, ::])  # обычный график
        axs[0, 0].plot(x, y, ',-', label=f"{j + 1} строка.")
        axs[0, 0].set(title="График с использованием функции plot:", xlabel='Номер элемента в строке',
                      ylabel='Значение элемента')
        axs[0, 0].grid()
        axs[0, 1].bar(x, y, 0.4, label=f"{j + 1} строка.")  # гистограмма
        axs[0, 1].set(title="График с использованием функции bar:", xlabel='Номер элемента в строке',
                      ylabel='Значение элемента')
        if n <= 10:
            axs[0, 1].legend(loc='lower right')
            axs[0, 1].legend(loc='lower right')
    explode = [0] * (n - 1)  # отношение средних значений от каждой строки
    explode.append(0.1)
    sizes = [round(np.mean(abs(F[i, ::])) * 100 / av, 1) for i in range(n)]
    axs[1, 0].set_title("График с использованием функции pie:")
    axs[1, 0].pie(sizes, labels=list(range(1, n + 1)), explode=explode, autopct='%1.1f%%', shadow=True)

    im, cbar = heatmap(F, list(range(n)), list(range(n)), ax=axs[1, 1], cmap="magma_r")
    texts = annotate_heatmap(im)
    axs[1, 1].set(title="Создание аннотированных тепловых карт:", xlabel="Номер столбца", ylabel="Номер строки")
    plt.suptitle("Использование библиотеки matplotlib")
    plt.tight_layout()
    plt.show()

    print('\nРабота программы завершена.')
except ValueError:  # ошибка на случай введения не числа в качестве порядка или коэффициента
    print('\nВведенный символ не является числом. Перезапустите программу и введите число.')