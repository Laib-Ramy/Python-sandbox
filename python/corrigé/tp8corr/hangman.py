import string
import random
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


SECRETS="""affix
avenue
awkward
beekeeper
boggle
cobweb
cycle
disavowE
duplex
equip
exodus
funny
galaxy
gossip
icebox
injury
ivory
jackpot
jelly
jockey
joking
joyful
jumbo
kayak
khaki
kiosk
lengths
lucky
luxury
lymph
nightclub
onyx
ovary
pajama
pneumonia
pshaw
puppy
scratch
staff
stretch
""".upper().split()

MAX_ERRORS=10

class Hangman(QDialog):
    def __init__(self, parent=None):
        super(Hangman, self).__init__(parent)
        letter_buttons=[QPushButton(s) for s in list(string.ascii_uppercase)]
        self.dict_buttons={b.text():b for b in letter_buttons}
        button_layout=QHBoxLayout()
        for b in letter_buttons:
            width = b.fontMetrics().boundingRect(b.text()).width() + 15
            b.setMaximumWidth(width)
            b.clicked.connect(self.letter_action(b.text()))
            button_layout.addWidget(b)
        self.word=QLabel('')
        self.word.setAlignment(Qt.AlignHCenter)
        self.word.setFont(QFont('Courier', 36))
        self.status=QLabel('')
        self.status.setAlignment(Qt.AlignHCenter)
        reset_button=QPushButton("Restart")
        reset_button.clicked.connect(self.reset)
        main_layout=QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.word)
        main_layout.addWidget(self.status)
        main_layout.addWidget(reset_button)
        self.setLayout(main_layout)
        # The state of the game is given by these variables:
        self.secret=''
        self.guessed=set()
        self.errors=0

    def keyPressEvent(self, event):
        c = event.text()
        self.letter_guessed(c.upper())

    def letter_action(self, c):
        def do_letter():
            self.letter_guessed(c)
        return do_letter

    def letter_guessed(self, c):
        b=self.dict_buttons[c]
        b.setEnabled(False)
        self.guessed.add(c)
        clear=self.cleartext()
        self.word.setText(clear)
        if c not in self.secret:
            self.errors+=1
        if self.errors>=MAX_ERRORS:
            self.end_game("You lost!")
        elif clear==self.secret:
            self.end_game("You won!")
        else:
            self.status.setText(f"Errors: {self.errors}/{MAX_ERRORS}")

    def end_game(self, msg):
        self.status.setText(msg)
        for _,b in self.dict_buttons.items():
            b.setEnabled(False)

    def reset(self):
        for _,b in self.dict_buttons.items():
            b.setEnabled(True)
        self.secret=random.choice(SECRETS)
        self.errors=0
        self.guessed.clear()
        self.word.setText(self.cleartext())
        self.status.setText('')

    def cleartext(self):
        return ''.join(c if c in self.guessed else '-' for c in self.secret)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    h = Hangman()
    h.reset()
    h.show()
    sys.exit(app.exec_())

    
