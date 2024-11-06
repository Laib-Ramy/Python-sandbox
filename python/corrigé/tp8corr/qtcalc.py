from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class Calculator(QDialog):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        layout = QGridLayout()

        self.edit_a = QLineEdit("")
        self.edit_b = QLineEdit("")
        self.button_add = QPushButton("+")
        self.button_sub = QPushButton("-")
        self.button_mul = QPushButton("*")
        self.button_div = QPushButton("/")
        self.label_ans=QLabel("")

        self.button_add.clicked.connect(self.do_add)
        self.button_sub.clicked.connect(self.do_sub)
        self.button_mul.clicked.connect(self.do_mul)
        self.button_div.clicked.connect(self.do_div)

        layout.addWidget(self.edit_a, 0, 0)
        layout.addWidget(self.edit_b, 1, 0)
        layout.addWidget(self.button_add, 0, 1)
        layout.addWidget(self.button_sub, 0, 2)
        layout.addWidget(self.button_mul, 1, 1)
        layout.addWidget(self.button_div, 1, 2)
        layout.addWidget(QLabel("Answer"), 0, 3)
        layout.addWidget(self.label_ans, 1, 3)
        self.setLayout(layout)

    def validateInput(self):
        try:
            a=float(self.edit_a.text())
            b=float(self.edit_b.text())
            return (a,b)
        except(ValueError):
            self.label_ans.setText('')
            alert("Non-numeric input")
            return None

    def do_add(self):
        v=self.validateInput()
        if v:
            self.label_ans.setText(str(v[0]+v[1]))

    def do_sub(self):
        v=self.validateInput()
        if v:
            self.label_ans.setText(str(v[0]-v[1]))

    def do_mul(self):
        v=self.validateInput()
        if v:
            self.label_ans.setText(str(v[0]*v[1]))

    def do_div(self):
        v=self.validateInput()
        if v:
            if v[1]:
                self.label_ans.setText(str(v[0]/v[1]))
            else:
                self.label_ans.setText('')
                alert('Division by zero')

def alert(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
