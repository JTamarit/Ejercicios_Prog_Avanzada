import sys

from PyQt6 import QtGui
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLineEdit, QPushButton, QFormLayout

import eyed3

class Window(QWidget):
    filename= "music/Enter_Sandman.mp3"
    audiofile = eyed3.load(filename)

    author = audiofile.tag.artist 
    album = audiofile.tag.album 
    track_num = str(audiofile.tag.track_num)
    title = audiofile.tag.title
    track = audiofile.tag.track_num
    genre = str(audiofile.tag.genre)

    font = QtGui.QFont()
    font.setFamily("Barlow")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('MP3 TAGS EDITOR')
        self.setFixedSize(QSize(300,200))
       
        self.save = QPushButton('Save')
        self.exit = QPushButton('Exit')
        self.save.setFont(Window.font)
        self.exit.setFont(Window.font)

        layout=QFormLayout()
        layout.addRow('Author:', QLineEdit(Window.author))
        layout.addRow('Album:', QLineEdit(Window.album))
        layout.addRow('Track num:', QLineEdit(Window.track_num))
        layout.addRow('Title:', QLineEdit(Window.title))
        layout.addRow('Genre:',QLineEdit(Window.genre))
        layout.addRow(self.save, self.exit)
        Window.audiofile.tag.save()
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
        


