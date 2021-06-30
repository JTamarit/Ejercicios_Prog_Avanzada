
from PyQt6.QtWidgets import (QMainWindow, QTextEdit,
        QFileDialog, QApplication)
from PyQt6.QtGui import  QAction
from pathlib import Path
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showFileDialog)

        savetags = QAction('Save tags', self)
        savetags.setShortcut('Ctrl+S')
        savetags.setStatusTip('Save tags')
        savetags.triggered.connect(self._save)

        quit_app= QAction('Quit',self)
        quit_app.setShortcut('Crtl+Q')
        quit_app.setStatusTip('Quit')
        quit_app.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(savetags)
        fileMenu.addAction(quit_app)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()


    def showFileDialog(self):

        home_directory = str(Path.home())
        filename = QFileDialog.getOpenFileName(self, 'Open file', home_directory,"Mp3 File (*.mp3)")

        if filename[0]:

            file = open(filename[0], 'r')

            with file:

                data = file.read()
                self.textEdit.setText(data)

    def _save(self):
        pass

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()