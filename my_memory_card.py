from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = []

questions.append(Question('В кааком году была выпущена игра cs2?', '2023', '2012', '2022', '2021'))
questions.append(Question('Самый популярный спорт в мире?', 'Футбол', 'Баскетбол', 'Хокей', 'Все одинаково=)'))
questions.append(Question('Страна в форме сапога на карте это?', 'Италия', 'Испания', 'Греция', 'Такой страны нету=('))
questions.append(Question('Человек это?', 'Существо биосоциальное', 'Существо социальное', 'Существо биологическое', 'Просто человек'))
questions.append(Question('Python это?', 'Самый популярный язык программирования', 'Самый распрастранённый язык программирования', 'Самый старый язык программирования', 'Самый новый язык программирования'))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memo Card')

window.resize(500, 350)

'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('В каком году была основана Москва?') # текст вопроса


RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке


RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 
AnsGroup = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправлиьно')
lb_correct = QLabel('Правильный ответ')
layout_answer = QVBoxLayout()
layout_answer.addWidget(result, alignment = Qt.AlignLeft)
layout_answer.addWidget(lb_correct, alignment = Qt.AlignCenter)
AnsGroup.setLayout(layout_answer)
RadioGroupBox.show()
AnsGroup.hide()

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroup)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)

# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым


window.setLayout(layout_card)
def show_results():
    RadioGroupBox.hide()
    AnsGroup.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    AnsGroup.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
#def start_test():
#    if btn_OK.text() == 'Ответить':
#        show_results()
#    else:
#        show_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    result.setText(res)
    show_results()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно')
def next_question():
    q = questions[randint(0, len(questions))]
    ask(q)
def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
btn_OK.clicked.connect(click_ok)
window.show()
app.exec()