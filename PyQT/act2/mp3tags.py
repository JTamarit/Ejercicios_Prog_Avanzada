import sys
import eyed3

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QFormLayout, QPushButton, QLineEdit
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QStatusBar


class Window(QMainWindow):
    

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('MP3 TAGS EDITOR')
        self.setFixedSize(QSize(300,200))
        self.load_tags()

        self.button_save= QPushButton('Save Changes')
        self.button_exit= QPushButton('Quit')

        self.artist = QLineEdit(self.audiofile.tag.artist)
        self.album = QLineEdit(self.audiofile.tag.album)
        self.track_num = QLineEdit(str(self.audiofile.tag.track_num))
        self.title = QLineEdit(self.audiofile.tag.title)
        self.genre= QLineEdit(str(self.audiofile.tag.genre.name))


        form_layout = QFormLayout()
        form_layout.addRow('Author:',self.artist)
        form_layout.addRow('Album:', self.album)
        form_layout.addRow('Track num:', self.track_num)
        form_layout.addRow('Title:', self.title)
        form_layout.addRow('Genre:', self.genre)

        form_layout.addRow(self.button_save, self.button_exit)
        self.button_exit.clicked.connect(self.close)
        self.button_save.clicked.connect(self._save)

        self.artist.textChanged.connect(self._update)
        self.album.textChanged.connect(self._update)
        self.track_num.textChanged.connect(self._update)
        self.title.textChanged.connect(self._update)
        self.genre.textChanged.connect(self._update)

        container = QWidget()
        container.setLayout(form_layout)
        self.setCentralWidget(container)
        self._create_status_bar()
        

    def _create_status_bar(self):
        status = QStatusBar()
        status.showMessage(self.filename)
        self.setStatusBar(status)

    def load_tags(self):

        self.filename= "music/Enter_Sandman.mp3"
        self.audiofile = eyed3.load(self.filename)
        

    def _update(self, input):

        if self.artist.textChanged:
            self.audiofile.tag.artist = str(input)
            print(self.audiofile.tag.artist)

        elif self.album.textChanged:
            self.audiofile.tag.album = str(input)
            print(self.audiofile.tag.album)

        elif self.track_num.textChanged:
            self.audiofile.tag.track_num =input
            print(self.audiofile.tag.track_num)

        elif self.title.textChanged:
            self.audiofile.tag.title = str(input)
            print(self.audiofile.tag.title)

        elif self.genre.textChanged:
            self.audiofile.tag.genre.name = input
            print(self.audiofile.tag.genre.name)

    def _save(self):

        self.audiofile.tag.artist = self.artist.text()
        self.audiofile.tag.album = self.album.text()
        self.audiofile.tag.track_num = tuple(self.track_num.text())
        self.audiofile.tag.title = self.title.text()
        self.audiofile.tag.genre.name = self.genre.text()

        self.audiofile.tag.save()
        print("\n Los tags guardados son:\n")
        print(self.audiofile.tag.artist)
        print(self.audiofile.tag.album)
        print(self.audiofile.tag.track_num)
        print(self.audiofile.tag.title)
        print(self.audiofile.tag.genre)
        print("Saved")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
