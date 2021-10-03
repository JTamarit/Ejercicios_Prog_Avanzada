from functools import partial
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget

ERROR_MSG = 'Error'

class View(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        self.general_layout = QVBoxLayout()
        self._central_widget.setLayout(self.general_layout)

        self._create_display()
        self._create_buttons()

    def _create_display(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.general_layout.addWidget(self.display)

    def _create_buttons(self):
        self.buttons = {}
        buttons_layout = QGridLayout()
        buttons = {'7': (0, 0),
                '8': (0, 1),
                '9': (0, 2),
                '/': (0, 3),
                'C': (0, 4),
                '4': (1, 0),
                '5': (1, 1),
                '6': (1, 2),
                '*': (1, 3),
                '(': (1, 4),
                '1': (2, 0),
                '2': (2, 1),
                '3': (2, 2),
                '-': (2, 3),
                ')': (2, 4),
                '0': (3, 0),
                '00': (3, 1),
                '.': (3, 2),
                '+': (3, 3),
                '=': (3, 4),
                }

        for btn_text, pos in buttons.items():
            self.buttons[btn_text] = QPushButton(btn_text)
            self.buttons[btn_text].setFixedSize(40, 40)
            buttons_layout.addWidget(self.buttons[btn_text], pos[0], pos[1])

        self.general_layout.addLayout(buttons_layout)

    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        return self.display.text()

    def clear_display(self):
        self.set_display_text('')

class Model:

    def __init__(self):
        pass

    def evaluate_expression(self, expression):
        try:
            result = str(eval(expression))
        except Exception:
            result = ERROR_MSG

        return result

class Controller:

    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._connect_signals()

    def _build_expression(self, sub_exp):
        if self._view.display_text() == ERROR_MSG:
            self._view.clear_display()

        expression = self._view.display_text() + sub_exp
        self._view.set_display_text(expression)

    def _calculate_result(self):
        result = self._model.evaluate_expression(self._view.display_text())
        self._view.set_display_text(result)

    def _connect_signals(self):
        for btn_text, btn in self._view.buttons.items():
            if btn_text not in {'=', 'C'}:
                btn.clicked.connect(partial(self._build_expression, btn_text))

        self._view.buttons['C'].clicked.connect(self._view.clear_display)
        self._view.buttons['='].clicked.connect(self._calculate_result)
        self._view.display.returnPressed.connect(self._calculate_result)

def main():
    calc = QApplication(sys.argv)

    view = View()  
    model = Model()
    controller = Controller(view, model)

    view.show()

    sys.exit(calc.exec())

if __name__ == '__main__':
    main()