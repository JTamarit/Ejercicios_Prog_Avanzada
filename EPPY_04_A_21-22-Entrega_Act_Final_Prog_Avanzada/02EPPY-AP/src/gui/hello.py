import functools
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout

def say_hi(who):
    if message.text():
        message.setText("")
    else:
        message.setText(f"Hello {who}")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Signals and slots')

layout = QVBoxLayout()

button = QPushButton('Say Hi!!!')
button.clicked.connect(functools.partial(say_hi, "Manolo"))

layout.addWidget(button)

message = QLabel('')
layout.addWidget(message)

window.setLayout(layout)
window.show()

sys.exit(app.exec())