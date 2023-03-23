"""
С клавиатуры вводятся два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
заполнение, а целенаправленное.
Вид матрицы А:
D   Е
С   В
Каждая из матриц B,C,D,E имеет вид:
     4
  3     1
     2
     
Вариант 7:
Формируется матрица F следующим образом:
если в С количество нулевых элементов в нечетных столбцах в области 4 больше,
чем количество нулевых  элементов в четных столбцах в области 1,
то поменять в В симметрично области 2 и 3 местами, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: ((F*A)– (K * AT)) .
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

from math import ceil
import random as r


def print_m(matrix):  # функция вывода матрицы
    matrix1 = list(map(list, zip(*matrix)))
    for i in range(len(matrix1)):
        c = len(max(list(map(str, matrix1[i])), key=len))
        matrix1[i] = [f'{elem:{c+1}d}' for elem in matrix1[i]]
    matrix1 = list(map(list, zip(*matrix1)))
    for row in matrix1:
        print(*row)


try:
    n = int(input('Введите число N: '))
    k = int(input('Введите число K: '))
    
    seredina = ceil(n / 2)                                       # Серидины матрицы
    A = [[r.randint(-10, 10) for i in range(n)] for j in range(n)]  # Задаём матрицу A
    A_dump = A.copy()                                            # Делаем копию матрицы А
    AT = [[0 for i in range(n)] for j in range(n)]               # Заготовка под транспонированную матрицу А
    F = A.copy()                                                 # Задаём матрицу F
    FA = [[0 for i in range(n)] for j in range(n)]               # Заготовка под результат умножения матрицы F на матрицу А
    KAT = [[0 for i in range(n)] for j in range(n)]              # Заготовка под результат умножения матрицы AT на коэффициент K
    vichit = [[0 for i in range(n)] for j in range(n)]           # Заготовка под результат вычитания двух матриц

    for i in range(n):                                           # Транспонируем матрицу А
        for j in range(n):
            AT[i][j] = A_dump[j][i]

    print('\nМатрица А:')
    print_m(A)
    print('\nТранспонированная А:')
    print_m(AT)

    if n % 2 == 1:
        E = [A[i][seredina - 1:n] for i in range(seredina)]
        C = [A[i][0:seredina] for i in range(seredina - 1, n)]
        B = [A[i][seredina - 1:n] for i in range(seredina - 1, n)]
    else:
        E = [A[i][seredina:n] for i in range(0, seredina)]
        C = [A[i][0:seredina] for i in range(seredina, n)]
        B = [A[i][seredina:n] for i in range(seredina, n)]

    zerov4 = 0
    zerov1 = 0
    for i in range(seredina): 
        for j in range(seredina):
            if (i <= j) and ((i + j + 1) <= seredina) and ((j + 1) % 2 == 1):
                if C[i][j] ==0 :
                    zerov4 += 1

    for m in range(seredina):
        for z in range(seredina):
            if (m <= z) and ((m + z + 1) >= seredina) and ((z + 1) % 2 == 0):
                if C[m][z] == 0 :
                    zerov1 += 1
            
    if zerov4 > zerov1:
        print(f'\nВ матрице "C" количество нулевых элементов в нечетных столбцах в области 4({zerov4})')
        print(f'больше чем количество нулевых  элементов в четных столбцах в области 1({zerov1})')
        print('поэтому симметрично меняем местами области 2 и 3 в "B".')
        
        for i in range(seredina):
            for j in range(seredina):
                if i >= j and (i+j+1) <= seredina:
                    B[i][j], B[(seredina - j) - 1][(seredina - i) - 1] = B[(seredina - j) - 1][(seredina - i) - 1], B[i][j] # Cимметрично меняем местами области 2 и 3 в В
                                
        if n % 2 == 1:
            for i in range(seredina, n):
                for j in range(seredina, n):
                    F[i][j] = B[i - (seredina-1)][j - (seredina-1)]
        else:
            for i in range(seredina, n):
                for j in range(seredina, n):
                    F[i][j] = B[i - (seredina)][j - (seredina)]
    
    else:
        print(f'\nВ матрице "C" количество нулевых элементов в нечетных столбцах в области 4({zerov4})')
        print(f'меньше чем количество нулевых  элементов в четных столбцах в области 1({zerov1}) или равно ей')
        print('поэтому несимметрично меняем местами области "C" и "E":')

                                                         #С и Е меняются местами несимметрично
        C, E = E, C  
        if n % 2 == 1:
            
            for i in range(seredina - 1, n):
                for j in range(seredina):
                    F[i][j] = C[i - (seredina - 1)][j]
                    
            for i in range(seredina):
                for j in range(seredina - 1, n):
                    F[i][j] = E[i][j - (seredina - 1)]
                    
        else:
            for i in range(seredina, n):
                for j in range(seredina):
                    F[i][j] = C[i - seredina][j]
                    
            for i in range(0, seredina):
                for j in range(seredina, n):
                    F[i][j] = E[i][j - seredina]
                    
    for i in range(n):
        for j in range(n):
            FA[i][j] = F[i][j] * A[i][j]
            KAT[i][j] = k * AT[i][j]


    for i in range(n):
        for j in range(n):
            vichit[i][j] = FA[i][j] - KAT[i][j]

                                                         # Вывод всех операций
    print('\nМатрица F:')
    print_m(F)
    print('\nРезультат F * A:')
    print_m(FA)
    print("\nРезультат K * АT:")
    print_m(KAT)
    '''print('\nРезультат (К * F) * А:')
    print_m(KFA)'''
    print('\nРезультат  F * А – K * AT:')
    print_m(vichit)
    print('\nРабота программы завершена.')
except ValueError:                                       # Если введено не число в качестве порядка или коэффициента
    print('\nВведенный символ не является числом. Перезапустите программу и введите число.')