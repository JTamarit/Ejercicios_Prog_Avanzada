import sys
import os
import requests
import cv2


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 351, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.city = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.city.setFont(font)
        self.city.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.city.setObjectName("city")
        self.gridLayout.addWidget(self.city, 0, 0, 1, 1)
        self.lineEditCity = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditCity.setFont(font)
        self.lineEditCity.setObjectName("lineEditCity")
        self.gridLayout.addWidget(self.lineEditCity, 0, 1, 1, 2)
        self.pushButton_current = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_current.setFont(font)
        self.pushButton_current.setObjectName("pushButton_current")
        self.gridLayout.addWidget(self.pushButton_current, 0, 3, 1, 1)
        self.temp = QtWidgets.QLabel(self.layoutWidget)
        self.temp.setFont(font)
        self.temp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.temp.setObjectName("temp")
        self.gridLayout.addWidget(self.temp, 1, 0, 1, 1)
        self.icon = QtWidgets.QLabel(self.layoutWidget)
        self.icon.setFont(font)
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap(""))
        self.icon.setScaledContents(True)
        self.icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 1, 1, 2, 1)
        self.feeltemp = QtWidgets.QLabel(self.layoutWidget)
        self.feeltemp.setFont(font)
        self.feeltemp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.feeltemp.setObjectName("feeltemp")
        self.gridLayout.addWidget(self.feeltemp, 1, 2, 1, 2)
        self.label_temp = QtWidgets.QLabel(self.layoutWidget)
        font.setPointSize(24)
        self.label_temp.setFont(font)
        self.label_temp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.gridLayout.addWidget(self.label_temp, 2, 0, 1, 1)
        self.label_feeltemp = QtWidgets.QLabel(self.layoutWidget)
        self.label_feeltemp.setFont(font)
        self.label_feeltemp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_feeltemp.setObjectName("label_feeltemp")
        self.gridLayout.addWidget(self.label_feeltemp, 2, 2, 1, 2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(250, 240, 158, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_clear = QtWidgets.QPushButton(self.widget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_quit = QtWidgets.QPushButton(self.widget)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout.addWidget(self.pushButton_quit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_quit.clicked.connect(MainWindow.close)
        self.pushButton_current.clicked.connect(self._go_weather)
        self.pushButton_clear.clicked.connect(self._clean_labels)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Open Weather App"))
        self.city.setText(_translate("MainWindow", "City"))
        self.pushButton_current.setStatusTip(_translate("MainWindow", "Push to get current weather. Shortcut: INTRO"))
        self.pushButton_current.setText(_translate("MainWindow", "Current Weather"))
        self.pushButton_current.setShortcut(_translate("MainWindow", "Return"))
        self.temp.setText(_translate("MainWindow", "Temp"))
        self.feeltemp.setText(_translate("MainWindow", "Feel Temp"))
        self.label_temp.setText(_translate("MainWindow", ""))
        self.label_feeltemp.setText(_translate("MainWindow", ""))
        self.pushButton_clear.setStatusTip(_translate("MainWindow", "Push for cleanning labels. Shortcut: CTRL + L"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_clear.setShortcut(_translate("MainWindow", "Meta+L"))
        self.pushButton_quit.setStatusTip(_translate("MainWindow", "Quit Application. Shortcut: CTRL + S"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))
        self.pushButton_quit.setShortcut(_translate("MainWindow", "Meta+S"))
    
    def _go_weather(self):

        city=str(self.lineEditCity.text())

        if city == "":
            self._show_popup_null_label()
            self.temp=""
            self.temp_feel=""
            self.filepath=""
        else:
            self._set_city(city)
            self._get_parameters_current()
            self._scrapper_7_forecast()
            self._get_parameters_forecast()
            
        self._set_labels()

    
    def _clean_labels(self):
        
        self.lineEditCity.setText("")
        self.temp=""
        self.temp_feel=""
        self.filepath=""
        self._set_labels()

    def _set_city(self,city):
        self.units="metric"
        self.api_key ="9a16a8e5458b6fdb0d040e46ee221bca"
        self.language="es"
        self._scrapper_current_weather(city)

    def _scrapper_current_weather(self,city):
        # Get current weather and coord of the city.
        
        endpoint=(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={self.units}&uk&lang={self.language}&APPID={self.api_key}")
        response= requests.get(endpoint)
        self.dict_current=response.json()
        
    def _scrapper_7_forecast(self):
         # Get 7 days forescast weather
        try:
            self.lat=self.dict_current['coord']['lat']
        except KeyError:
            return
        self.lon=self.dict_current['coord']['lon']
        endpoint_7days=(f"https://api.openweathermap.org/data/2.5/onecall?lat={self.lat}&lon={self.lon}&units={self.units}&exclude=hourly,minutely&appid={self.api_key}")
        response_7days= requests.get(endpoint_7days)
        self.dict_7days=response_7days.json()
        print(self.dict_7days)       
        
    def _get_parameters_current(self):

        try:
            icon_weather=self.dict_current['weather'][0]['icon']
        except KeyError:
            self._show_popup_city_notfound()
            self._clean_labels()
            return
        file_icon=(f"http://openweathermap.org/img/w/{icon_weather}.png")
        _path=os.path.join("res","weathericon.png")
        f=open(_path,'wb')
        response_icon=requests.get(file_icon)
        f.write(response_icon.content)
        f.close
        self.temp = str(round(self.dict_current['main']['temp']))
        self.temp_feel=str(round(self.dict_current['main']['feels_like']))
        self.filepath=_path
        
        

        

    def _get_parameters_forecast(self):
        
        try:
            self.dict_7days
        except AttributeError:
            return
        print(self.dict_7days)  
        

    def _set_labels(self):
        _translate = QtCore.QCoreApplication.translate
        self.icon.setPixmap(QtGui.QPixmap(os.path.join(self.filepath)))
        self.label_temp.setText(_translate("MainWindow", self.temp))
        self.label_feeltemp.setText(_translate("MainWindow", self.temp_feel))

    def _show_popup_null_label(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Error") 
        dlg.setText("City can't be null.\nPlease enter a city name")
        dlg.setIcon(QMessageBox.Icon.Warning)
        button = dlg.exec()

    def _show_popup_city_notfound(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Error") 
        dlg.setText("City not found or doesn't exit.\nTry again")
        dlg.setIcon(QMessageBox.Icon.Warning)
        button = dlg.exec()


def main():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
