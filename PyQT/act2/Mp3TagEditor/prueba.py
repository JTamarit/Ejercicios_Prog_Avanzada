# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mp3tageditor(object):
    def setupUi(self, mp3tageditor):
        mp3tageditor.setObjectName("mp3tageditor")
        mp3tageditor.resize(549, 407)
        self.centralwidget = QtWidgets.QWidget(mp3tageditor)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(19, 19, 501, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_3)
        self.textEdit_4 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_4.setObjectName("textEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_4)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(290, 340, 231, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        mp3tageditor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mp3tageditor)
        self.statusbar.setObjectName("statusbar")
        mp3tageditor.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(mp3tageditor)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(mp3tageditor)
        QtCore.QMetaObject.connectSlotsByName(mp3tageditor)

    def retranslateUi(self, mp3tageditor):
        _translate = QtCore.QCoreApplication.translate
        mp3tageditor.setWindowTitle(_translate("mp3tageditor", "mp3tageditor"))
        self.label.setText(_translate("mp3tageditor", "Author"))
        self.label_2.setText(_translate("mp3tageditor", "Album"))
        self.label_3.setText(_translate("mp3tageditor", "Track"))
        self.label_4.setText(_translate("mp3tageditor", "Image"))
        self.pushButton_2.setText(_translate("mp3tageditor", "Edit"))
        self.pushButton.setText(_translate("mp3tageditor", "Quit"))
        self.actionQuit.setText(_translate("mp3tageditor", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mp3tageditor = QtWidgets.QMainWindow()
    ui = Ui_mp3tageditor()
    ui.setupUi(mp3tageditor)
    mp3tageditor.show()
    sys.exit(app.exec())