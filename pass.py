from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit, QListWidget
from random import *

app = QApplication([])
main_win = QWidget()

main_win.resize(700,500)
main_win.setWindowTitle('The password game')

main_layout = QVBoxLayout()
group = QHBoxLayout()
er  = QVBoxLayout()

question = QLabel('Введите пароль.')
enter = QLineEdit()
btn = QPushButton('Ок')
error = QListWidget()

main_layout.addWidget(question, alignment = Qt.AlignCenter)
group.addWidget(enter, alignment = Qt.AlignTop)
group.addWidget(btn,alignment = Qt.AlignTop)
er.addWidget(error,alignment = Qt.AlignTop)
main_layout.addLayout(group)
main_layout.addLayout(er)




main_win.setLayout(main_layout)

main_win.show()
app.exec_()
