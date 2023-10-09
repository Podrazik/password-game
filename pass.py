from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QListWidget, QLineEdit, QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox)
from pygame import *

mixer.init()
bad = mixer.Sound('erro.mp3')

def ask1():
    answer = enter.text()
    answer = answer.replace(" ", "")
    if len(answer) <= 5:
        error.addItem("! Длина пароля должна быть больше пяти без пробелов")
        bad.play()
    else:
        error.clear()
        return True


def ask2():
    a = ask1()
    if a:
        letter = 0
        answer = enter.text()
        for i in "ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮQWERTYUIOPLKJHGFDSAZXCVBNM":
            if i in answer:
                letter = 1
        if not letter:
            error.addItem("! Надо заглавную букву")
            bad.play()
        else:
            error.clear()
            return True


def ask3():
    a = ask2()
    if a:
        number = False
        answer = enter.text()
        for i in "IXVCMLDХСМ":
            if i in answer:
                number = True
        if not number:
            error.addItem("! Надо римскую цифру")
            bad.play()
        else:
            error.clear()
            return True


def ask4():
    a = ask3()
    if a:
        food = False
        answer = enter.text()
        if answer.find("пельмени") != -1 or answer.find('суп') != -1 or answer.find("котлета") != -1:
            food = True
        if not food:
            error.addItem("! На выбор добавьте еду из списка: пельмени, суп, котлета")
            bad.play()
        else:
            error.clear()
            return True


def ask5():
    a = ask4()
    if a:
        nok = False
        answer = enter.text()
        if answer.find("17640") != -1:
            nok = True
        if not nok:
            error.addItem("! Добавьте наименьшее общее кратное для 360, 245 и 18")
            bad.play()
        else:
            error.clear()
            return True


def ask6():
    a = ask5()
    if a:
        rim = False
        answer = enter.text()
        if answer.find("XXC") != -1 or answer.find('ХХС') != -1:
            rim = True
        if not rim:
            error.addItem("! Запишите сумму всех целых чисел от 1 до 200 в римской записи")
            bad.play()
        else:
            error.clear()
            return True


def ask7():
    a = ask6()
    if a:
        binar = False
        answer = enter.text()
        if answer.find("21") != -1:
            binar = True
        if not binar:
            error.addItem("! Переведите число 10101 из двоичной системы счисления в десятичную")
            bad.play()
        else:
            error.clear()
            return True


def ask8():
    a = ask7()
    if a:
        sy = False
        answer = enter.text()
        if answer.find("сы") != -1:
            sy = True
        if not sy:
            error.addItem("! Добавьте русскую транскрипцию 21-ой буквы китайского алфавита чжуинь")
            bad.play()
        else:
            error.clear()
            return True


def ask9():
    a = ask8()
    if a:
        country = False
        answer = enter.text()
        answer.lower()
        if answer.find('вашингтон') != -1 or answer.find('washington') != -1:
            country = True
        if not country:
            error.addItem("! Укажите столицу страны с самым большим ВВП")
            bad.play()
        else:
            error.clear()
            return True


def ask10():
    a = ask9()
    if a:
        him = False
        answer = enter.text()
        if answer.find("NH4Cl") != -1:
            him = True
            last_mes = QMessageBox()
            last_mes.setWindowTitle('Спасибо!')
            last_mes.setText('Вы успешно прошли регистрацию!')
            last_mes.exec()
        if not him:
            error.addItem("! Результат реакции соляной кислоты и аммиака")
            bad.play()
        else:
            error.clear()
            return True


app = QApplication([])
main_win = QWidget()

main_win.resize(700, 500)
main_win.setWindowTitle('Регистрация на Госуслугах')

main_layout = QVBoxLayout()
group = QHBoxLayout()
er = QVBoxLayout()

question = QLabel('Введите пароль.')
enter = QLineEdit()
btn = QPushButton('Ок')
error = QListWidget()

main_layout.addWidget(question, alignment=Qt.AlignCenter)
group.addWidget(enter, alignment=Qt.AlignTop)
group.addWidget(btn, alignment=Qt.AlignTop)
er.addWidget(error, alignment=Qt.AlignTop)

main_layout.addLayout(group)
main_layout.addLayout(er)

btn.clicked.connect(ask10)

main_win.setLayout(main_layout)
main_win.show()
app.exec_()
