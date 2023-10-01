"""
Лабораторная работа включает в себя два задания:
1) написать программу в соответствии со своим вариантом задания.
2) усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

Вариант 7:
Дана квадратная матрица. Сформировать все возможные варианты данной матрицы путём перестановки
элементов главной и побочной диагонали в каждой строке.

Дополнительным условием будет ограничение по перестановке только чётных строк.
Нужно вывести матрицы и их параметры и команду с наибольшой суммой элементов главной диагонали.
"""

import itertools
import copy
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



# класс
class MatrixClass(object):
    # атрибуты
    matrix = [[]]
    matrices = []
    sum = []

    # методы
    # инициализация
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrices = []
        self.sum = []

    # поиск в матрице пар элементов главной и побочной диагонали
    def gen_matrix(self, matrix):
        two_elem = []
        for row in range(len(self.matrix)):
            if row != len(self.matrix[row]) - 1 - row:
                two_elem.append([self.matrix[row][row], self.matrix[row][len(self.matrix) - 1 - row]])
                two_elem.append([self.matrix[row][len(self.matrix) - 1 - row], self.matrix[row][row]])
        return two_elem

    # поиск в чётных строках матрицы пар элементов главной и побочной диагонали
    def gen_matrix_even_row(self, matrix):
        two_elem = []
        for row in range(len(matrix)):
            if (row + 1) % 2 == 0:
                two_elem.append([matrix[row][row], matrix[row][len(matrix) - 1 - row]])
                two_elem.append([matrix[row][len(matrix) - 1 - row], matrix[row][row]])
        return two_elem

    # вывод суммы главной диагонали матрицы
    def get_parameters(self, matrix):
        sum = 0
        for i in range(len(matrix)):
            sum += matrix[i][i]
        return sum

    # вывод списка матриц
    def print_matrices(self):
        print('\nМатрицы:')
        for i in range(len(self.matrices)):
            print('Матрица №' + str(i + 1))
            for row in self.matrices[i]:
                print("".join(['{:<5}'.format(item) for item in row]))
            self.sum.append(self.get_parameters(self.matrices[i]))
            print("Сумма элементов главной диагонали = " + str(self.sum[i]) + '\n')
            print()

    # вывод матрицы с максимальной суммой главной диагонали
    def print_matrix_max_sum(self):
        # Вывод таблицы
        print('\nМатрица с наибольшей суммой элементов главной диагонали:')
        max_index = self.sum.index(max(self.sum))
        print('Матрица №' + str(max_index + 1))
        for row in self.matrices[max_index]:
            print("".join(['{:<5}'.format(item) for item in row]))
        print("Сумма элементов главной диагонали = " + str(self.sum[max_index]) + '\n')
        print()

    # запуск программы
    def change_el_primary_secondary_diagonal(self):
        m = copy.deepcopy(self.matrix)  # копируем матрицу, чтобы данные были новыми, а не ссылкой на старые
        if len(m) < 4:  # если размер матрицы меньше 4, то в программе нет смысла
            print('\nМатрицы:')
            print('Матрица №1')
            for i in range(len(m)):
                print("".join(['{:<5}'.format(item) for item in m[i]]))
            print("Сумма элементов главной диагонали = " + str(self.get_parameters(m)) + '\n')
            print()
            print('\nРабота программы завершена успешно.')
            exit()

        pairs = self.gen_matrix_even_row(m)  # генерируем возможное пары кажой строки
        all_combs = list(itertools.permutations(pairs, len(m) // 2))  # формируем всевозможные комбинаций пар элементов диагонали каждоый строки
        combs = []  # список подходящих комбо

        # проходимся по всем комбинациям
        for comb in all_combs:
            count = 0  # счётчик сходств
            for j in range(len(m) // 2):  # проходимся по чётным строкам
                # в каждой строке может быть только два варианта расположения элементов
                if comb[j] == pairs[j * 2] or comb[j] == pairs[j * 2 + 1]:  # если один из двух подходит
                    count += 1  # то засчитываем
            if count == len(m) // 2:  # если всё сошлось, добивим комбинацию в список подходящих
                combs.append(comb)

        for comb in combs:
            new_matrix = copy.deepcopy(m)  # опять же сделаем дубликат матрицы
            k = 0  # номер комбинации строки (для матриц нечётного размера)
            for j in range(1, len(new_matrix), 2):
                if j != len(new_matrix) - 1 - j:  # если мы не в центре в нечётной матрицы
                    new_matrix[j][j] = comb[k][0]
                    new_matrix[j][len(new_matrix) - 1 - j] = comb[k][1]
                k += 1
                # иначе j будет на 1 больше, чем k
                # т.к. центр не может иметь пары, а k есть счётчик пар

            equals = False # метка равности на случай одинаковых элементов по строке диагонали
            for matr in self.matrices:
                if (matr == new_matrix).all() == True: # если такая матрица уже есть в списке
                    equals = True # то помечаем это
            if not equals: # если метки равности нет, значит мы не повторимся
                self.matrices.append(new_matrix)  # добавим матрицу в список результатов



matrix_test = np.random.randint(10, size=(10, 10))


# графическая оболочка

window = Tk()
window.title("8 лабораторная работа")
window.geometry('600x450')
window.resizable(False, False)

def start():
    size = int(txt.get())
    if size < 4:
        messagebox.showerror('Внимание!', 'Ошибка: Размер матрицы не может быть меньше 4!')
    else:
        matrix_test = np.random.randint(10, size=(size, size))
        print('\nСгенерированная матрица:')
        for row in matrix_test:
            print("".join(['{:<5}'.format(item) for item in row]))
        print()
        task = MatrixClass(matrix_test) # создаём объект класса матрицы
        task.change_el_primary_secondary_diagonal() # запускаем в работу на алгоритм согласно варианту
        task.print_matrices() # выводим все возможные варианты матрицы
        task.print_matrix_max_sum() # выводим матрицу с наибольшей суммой по главной диагонали
        print('\nРабота программы завершена успешно.')

        text_max.configure(state='normal')
        text_result.delete(1.0, END)
        for i in range(len(task.matrices)):
            text_result.insert(END, 'Матрица №' + str(i + 1))
            text_result.insert(END, "\n")
            for row in task.matrices[i]:
                text_result.insert(END, "".join(['{:<5}'.format(item) for item in row]))
                text_result.insert(END, "\n")
            task.sum.append(task.get_parameters(task.matrices[i]))
            text_result.insert(END, "Сумма элементов главной диагонали = " + str(task.sum[i]) + '\n')
            text_result.insert(END, "\n")
            text_max.configure(state='disabled')

        text_max.configure(state='normal')
        text_max.delete(1.0, END)
        text_max.insert(END, 'Матрица с наибольшей суммой элементов главной диагонали:')
        max_index = task.sum.index(max(task.sum))
        text_max.insert(END, '\nМатрица №' + str(max_index + 1) + '\n')
        for row in task.matrices[max_index]:
            text_max.insert(END, "".join(['{:<5}'.format(item) for item in row]))
            text_max.insert(END, "\n")
        text_max.insert(END, "Сумма элементов главной диагонали = " + str(task.sum[max_index]) + '\n')
        text_max.configure(state='disabled')

frame_generate = LabelFrame(window, text='Инициализация')
frame_generate.grid(column=0, row=0)
lbl_size = Label(frame_generate, text="Введите размер квадратной матрицы:")
lbl_size.grid(column=0, row=0)
txt = Entry(frame_generate, width=10)
txt.grid(column=0, row=1)
btn = Button(frame_generate, text="Старт", command=start)
btn.grid(column=0, row=2)

lbl_result = Label(window, text="Результат:")
lbl_result.grid(column=0, row=3)
text_result = Text(window, width=74, height=10)
text_result.grid(column=0, row=4)

lbl_max = Label(window, text="Матрица с наибольшей суммой элементов главной диагонали:")
lbl_max.grid(column=0, row=5)
text_max = Text(window, width=74, height=8, state='disabled')
text_max.grid(column=0, row=6)

window.mainloop()