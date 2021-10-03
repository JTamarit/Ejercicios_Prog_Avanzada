from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton

Form, Window = uic.loadUiType("form.ui")

app = QApplication([])
window = Window()
window = QPushButton("Push Me")
form = Form()
form.setupUi(window)
window.show()
app.exec()