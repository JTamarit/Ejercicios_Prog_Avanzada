import sys
import eyed3

from PyQt6.QtCore import  QSize
from PyQt6.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QFileDialog, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QStatusBar
from PyQt6 import QtGui
from pathlib import Path


class Window(QMainWindow):
    

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('MP3 TAGS EDITOR')
        self.setFixedSize(QSize(450,225))
        
        self._open_file()
        self._load_tags(self.filename)

        self.artist = QLineEdit(self.audiofile.tag.artist)
        self.album = QLineEdit(self.audiofile.tag.album)
        self.song_num = QLineEdit(str(self.audiofile.tag.track_num[0]))
        self.cd_num = QLineEdit(str(self.audiofile.tag.track_num[1]))
        self.title = QLineEdit(self.audiofile.tag.title)
        self.genre= QLineEdit(str(self.audiofile.tag.genre))
        self.date= QLineEdit(str(self.audiofile.tag.original_release_date))

        vertical_layout = QVBoxLayout()

        grid= QGridLayout()
        grid.setSpacing(2)
        grid.addWidget(QLabel('Title'),0,0)
        grid.addWidget(self.title,0,1,1,5)
        grid.addWidget(QLabel('Artist'),1,0)
        grid.addWidget(self.artist,1,1,1,2)
        grid.addWidget(QLabel('Album'),1,3)
        grid.addWidget(self.album,1,4,1,5)
        grid.addWidget(QLabel('Genre'),2,0)
        grid.addWidget(self.genre, 2,1,1,2)
        grid.addWidget(QLabel('Date'),2,3)
        grid.addWidget(self.date, 2,4)
        grid.addWidget(QLabel('Track Number'),3,0)
        grid.addWidget(self.song_num, 3,1)
        grid.addWidget(QLabel('CD Number'),3,3)
        grid.addWidget(self.cd_num,3,4)

        horz_layout=QHBoxLayout()
        self.button_save= QPushButton('Save Changes')
        self.button_exit= QPushButton('Quit')
        
        horz_layout.addStretch(1)
        horz_layout.addWidget(self.button_save)
        horz_layout.addWidget(self.button_exit)
    
        self.button_exit.clicked.connect(self.close)
        self.button_save.clicked.connect(self._save)
    
        vertical_layout.addLayout(grid)
        vertical_layout.addLayout(horz_layout)
        container = QWidget()
        container.setLayout(vertical_layout)
        self.setCentralWidget(container)
        self._create_menu()
        self._create_status_bar()
    
    def _create_menu(self):
        self.menu = self.menuBar().addMenu("&File")
        self.menu.addAction('Open mp3 File', self._open_file)
        self.menu.addAction('Save',self._save)
        self.menu.addAction('&Quit', self.close)

    def _create_status_bar(self):
        status = QStatusBar()
        status.showMessage(self.filename)
        self.setStatusBar(status)

    def _load_tags(self,filename):

        self.audiofile = eyed3.load(filename)
    
    def _open_file(self):

        home_directory = str(Path.home())
        self.filename = QFileDialog.getOpenFileName(self, 'Open file', home_directory,"Mp3 File (*.mp3)")[0]
        return self.filename
        

    def _update(self, input):

        if self.artist.textChanged:
            self.audiofile.tag.artist = input
            print (self.audiofile.tag.artist)

        elif self.album.textChanged:
            self.audiofile.tag.album = input
            print(self.audiofile.tag.album)

        elif self.song_num.textChanged:
            self.audiofile.tag.track_num[0] = input
            print (self.audiofile.tag.track_num[0])
        
        elif self.cd_num.textChanged:
            self.audiofile.tag.track_num[1] = input
            print (self.audiofile.tag.track_num[1])
        

        elif self.title.textChanged:
            self.audiofile.tag.title = input
            print(self.audiofile.tag.title)

        elif self.genre.textChanged:
            self.audiofile.tag.genre= input
            print(self.audiofile.tag.genre)
        
        elif self.date.textChanged:
            self.audiofile.tag.original_release_date= input
            print(self.audiofile.tag.original_release_date)

    def _save(self):

        self.audiofile.tag.artist = self.artist.text()
        self.audiofile.tag.album = self.album.text()
        self.audiofile.tag.track_num = tuple([(str(self.song_num.text())), str((self.cd_num.text()))])
        self.audiofile.tag.title = self.title.text()
        self.audiofile.tag.genre= self.genre.text()
        self.audiofile.tag.original_release_date = (str(self.date.text()))

        self.audiofile.tag.save()

        print("\n Los tags guardados son:\n")

        print((str(self.date.text)))
        
        print(self.audiofile.tag.artist)
        print(self.audiofile.tag.album)
        print(self.audiofile.tag.track_num)
        print(self.audiofile.tag.title)
        print(self.audiofile.tag.genre)
        print(self.audiofile.tag.original_release_date)
        print("Saved")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
