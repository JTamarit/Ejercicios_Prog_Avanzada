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

        autor = QLineEdit(self.author)
        album = QLineEdit(self.album)
        track_num = QLineEdit(self.track_num)
        title = QLineEdit(self.title)
        genre = QLineEdit(self.genre)

        form_layout = QFormLayout()
        form_layout.addRow('Author:', autor)
        form_layout.addRow('Album:', album)
        form_layout.addRow('Track num:', track_num)
        form_layout.addRow('Title:', title)
        form_layout.addRow('Genre:', genre)
        form_layout.addRow(self.button_save, self.button_exit)
        self.button_exit.clicked.connect(self.close)
        self.button_exit.clicked.connect(self.save)
        autor.textChanged.connect(self._update)
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
        self.author = self.audiofile.tag.artist 
        self.album = self.audiofile.tag.album 
        self.track_num = str(self.audiofile.tag.track_num)
        self.title = self.audiofile.tag.title
        self.track = self.audiofile.tag.track_num
        self.genre = str(self.audiofile.tag.genre)


    def _update(self, input):
        
        self.audiofile.tag.author=input
        print(self.audiofile.tag.author)
        
    def save(self): 
        self.audiofile.tag.save()
        print("Saved")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
