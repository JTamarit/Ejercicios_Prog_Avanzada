# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.1.1

import os
import requests
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 351)
        self.filepath=""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(350, 230, 61, 32))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 70, 351, 101))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.city = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.city.setFont(font)
        self.city.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.city.setObjectName("city")
        self.gridLayout.addWidget(self.city, 0, 0, 1, 1)
        self.lineEditCity = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.lineEditCity.setFont(font)
        self.lineEditCity.setObjectName("lineEditCity")
        self.gridLayout.addWidget(self.lineEditCity, 0, 1, 1, 2)
        self.pushButton_current = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.pushButton_current.setFont(font)
        self.pushButton_current.setObjectName("pushButton_current")
        self.gridLayout.addWidget(self.pushButton_current, 0, 3, 1, 1)
        self.temp = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.temp.setFont(font)
        self.temp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.temp.setObjectName("temp")
        self.gridLayout.addWidget(self.temp, 1, 0, 1, 1)
        self.icon = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.icon.setFont(font)
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap(""))
        self.icon.setScaledContents(True)
        self.icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 1, 1, 2, 1)
        self.feeltemp = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.feeltemp.setFont(font)
        self.feeltemp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.feeltemp.setObjectName("feeltemp")
        self.gridLayout.addWidget(self.feeltemp, 1, 2, 1, 2)
        self.label_temp = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.label_temp.setFont(font)
        self.label_temp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.gridLayout.addWidget(self.label_temp, 2, 0, 1, 1)
        self.label_feeltemp = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.label_feeltemp.setFont(font)
        self.label_feeltemp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_feeltemp.setObjectName("label_feeltemp")
        self.gridLayout.addWidget(self.label_feeltemp, 2, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_quit.clicked.connect(MainWindow.close)
        self.pushButton_current.clicked.connect(self._update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather App"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))
        self.city.setText(_translate("MainWindow", "City"))
        self.pushButton_current.setText(_translate("MainWindow", "Current Weather"))
        self.temp.setText(_translate("MainWindow", "Temp"))
        self.feeltemp.setText(_translate("MainWindow", "Feel Temp"))
        self.label_temp.setText(_translate("MainWindow", "TextLabel"))
        self.label_feeltemp.setText(_translate("MainWindow", "TextLabel"))

    def _update(self):
        self._scrap()
        _translate = QtCore.QCoreApplication.translate
        self.icon.setPixmap(QtGui.QPixmap(os.path.join(self.filepath)))
        self.label_temp.setText(_translate("MainWindow", self.temp))
        self.label_feeltemp.setText(_translate("MainWindow", self.temp_feel))

    def _show_popup(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Error") 
        dlg.setText("City can't be null")
        dlg.setIcon(QMessageBox.Icon.Warning)
        button = dlg.exec()
        
        

    def _scrap(self):

        city=str(self.lineEditCity.text())
        if city == "":
            self._show_popup()
            self.temp=""
            self.temp_feel=""
            self.filepath=""
        else:
            units="metric"
            api_key ="9a16a8e5458b6fdb0d040e46ee221bca"
            language="es"
            endpoint=(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&uk&lang={language}&APPID={api_key}")
            response= requests.get(endpoint)
            diccionario=response.json()
            print(diccionario)
            icon_weather=diccionario['weather'][0]['icon']
            file_icon=(f"http://openweathermap.org/img/w/{icon_weather}.png")
            f=open('res/weathericon.png','wb')
            response_icon=requests.get(file_icon)
            f.write(response_icon.content)
            f.close
            self.temp = str(round(diccionario['main']['temp']))
            self.temp_feel=str(round(diccionario['main']['feels_like']))
            self.filepath="res/weathericon.png"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
