import os
import random
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def dismiss(win):
    win.grab_release()
    win.destroy()


def openlist():
    try:
        text = open(r'C:\лаба\pil.txt', 'r+')
        return text
    except FileNotFoundError:
        try:
            os.mkdir(r'C:\лаба')
            text = open(r'C:\лаба\pil.txt', 'w')
            text.close()
            text = open(r'C:\лаба\pil.txt', 'r+')
            return text
        except FileNotFoundError:
            text = open(r'C:\лаба\pil.txt', 'r+')
            return text


class game:
    def __init__(self, main):

        self.count = 0
        self.main = main
        self.account = {}
        self.first_click = True
        self.txt = Label(text='Введите логин и пароль', font='Batang 22 bold')
        self.txtlog = Label(text='Логин', font='Batang 17 bold')
        self.txtpar = Label(text='Пароль', font='Batang 17 bold')
        self.login = ttk.Entry(width=30, justify='center', font='Batang 10 bold')
        self.password = ttk.Entry(width=30, justify='center', font='Batang 10 bold')
        self.button_reg = ttk.Button(text='Регистрация', command=lambda: self.regist())
        self.button_avt = ttk.Button(text='Авторизация', command=lambda: self.authorization())

        self.txt.place(x=130, y=50)
        self.txtlog.place(x=270, y=100)
        self.txtpar.place(x=270, y=180)
        self.login.place(x=205, y=140, height=40)
        self.password.place(x=205, y=220, height=40)
        self.button_reg.place(x=150, y=300)
        self.button_avt.place(x=410, y=300)


    def authorization(self):
        s_l = self.login.get()
        s_p = self.password.get()

        if len(s_p) == 0 and len(s_l) == 0:
            messagebox.showwarning(title='Ошибка', message='Введите логин и пароль')
        elif len(s_l) == 0:
            messagebox.showwarning(title='Ошибка', message='Введите логин')
        elif len(s_p) == 0:
            messagebox.showwarning(title='Ошибка', message='Введите пароль')

        else:
            file = openlist()
            a = file.readline()[:-1].split(' ')

            while True:
                if a != ['']:
                    self.account[a[0]] = a[1]
                    a = file.readline()[:-1].split(' ')
                else:
                    break

            f_reg = False
            f_p = True
            for i in self.account.items():
                l, p = i
                if s_l == l and s_p == p:
                    f_reg = True
                    break
                elif s_l == l and s_p != p:
                    f_p = False

            if f_reg:
                win = Toplevel()
                win.geometry('400x120+520+320')
                win.title('Авторизация завершена')
                win.grab_set()
                win.protocol('WM_DELETE_WINDOW', lambda: dismiss(win))

                Label(win, text='Вы успешно авторизовались', font='Batang 15 bold').place(x=60, y=20)
                ttk.Button(win, text='Начать игру', command=lambda: self.igra(win)).place(x=160, y=70)

            elif not f_p:
                messagebox.showwarning(title='Ошибка', message='Неверный пароль')
            else:
                messagebox.showwarning(title='Ошибка', message='Аккаунт не зарегестрирован')

    def regist(self):
        win = Toplevel()
        win.geometry('620x350+360+210')
        win.title('Регистрация')
        win.resizable(False, False)
        win.protocol('WM_DELETE_WINDOW', lambda: dismiss(win))
        win.grab_set()

        login = ttk.Entry(win, width=30, justify='center', font='Batang 10 bold')
        password = ttk.Entry(win, width=30, justify='center',font='Batang 10 bold')
        txtlog = Label(win, text='Логин', font='Batang 17 bold')
        txtpar = Label(win, text='Пароль', font='Batang 17 bold')
        txt = Label(win, text='Введите логин и пароль', font='Batang 22 bold')
        button_reg = ttk.Button(win, text='Зарегистрироваться', command=lambda: registration())


        txt.place(x=150, y=50)
        txtlog.place(x=270, y=100)
        txtpar.place(x=270, y=180)
        login.place(x=205, y=140, height=40)
        password.place(x=205, y=220, height=40)
        button_reg.place(x=240, y=300)

        def registration():
            s_l = login.get()
            s_p = password.get()


            if len(s_p) == 0 and len(s_l) == 0:
                messagebox.showwarning(title='Ошибка', message='Введите логин и пароль')
            elif len(s_l) == 0:
                messagebox.showwarning(title='Ошибка', message='Введите логин')
            elif len(s_p) == 0:
                messagebox.showwarning(title='Ошибка', message='Введите пароль')
            else:
                file = openlist()
                a = file.readline()[:-1].split(' ')

                while True:
                    if a != ['']:
                        self.account[a[0]] = a[1]
                        a = file.readline()[:-1].split(' ')
                    else:
                        break

                f_reg = False

                for i in self.account.items():
                    l, p = i
                    if s_l == l:
                        f_reg = True

                if not f_reg:
                    file = openlist()
                    file.seek(0, os.SEEK_END)
                    file.write(f'{s_l} {s_p}\n')
                    file.close()

                    for widget in win.winfo_children():
                        widget.destroy()

                    Label(win, text='Регистрация прошла успешно', font='Batang 20 bold').place(x=100, y=100)
                    win.after(1000, lambda: (win.destroy(), win.grab_release()))
                else:
                    messagebox.showwarning(title='Ошибка', message='Этот аккаунт уже зарегестрирован')


    def igra(self, window):
        window.destroy()
        root.title('Поле')
        brow = bcol = 8
        cellsz = 50

        canvas = Canvas(self.main, width=cellsz * brow, height=cellsz * bcol)

        cell_colors = ['white', 'black']
        ci = 0  # color index

        for row in range(brow):
            for col in range(bcol):
                x1, y1 = col * cellsz, row * cellsz
                x2, y2 = col * cellsz + cellsz, row * cellsz + cellsz
                canvas.create_rectangle((x1, y1), (x2, y2), fill=cell_colors[ci])

                ci = not ci

            ci = not ci
        self.main.geometry('399x399+560+100')
        canvas.pack()


root = Tk()
root.title('Авторизация')
root.geometry('620x350+360+210')
root.resizable(False, False)

game(root)

root.mainloop()