import sys
import eyed3
 
from PyQt6.QtCore import  QSize
from PyQt6.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QFileDialog, QPushButton, QLineEdit, QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QStatusBar
from PyQt6 import QtGui
from pathlib import Path
 

class View(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('MP3 TAGS EDITOR')
        self.setFixedSize(QSize(450,225))
 
        vertical_layout = QVBoxLayout()
        grid= QGridLayout()
        self.artist = QLineEdit('')
        self.album = QLineEdit('')
        self.song_num = QLineEdit(str(''))
        self.cd_num = QLineEdit(str(''))
        self.title = QLineEdit('')
        self.genre= QLineEdit(str(''))
        self.date= QLineEdit(str(''))
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
        self.button_open = QPushButton('Open file')
        self.button_save= QPushButton('Save Changes')
        self.button_exit= QPushButton('Quit')
        
        horz_layout.addStretch(1)
        horz_layout.addWidget(self.button_open)
        horz_layout.addWidget(self.button_save)
        horz_layout.addWidget(self.button_exit)
    
        vertical_layout.addLayout(grid)
        vertical_layout.addLayout(horz_layout)
        container = QWidget()
        container.setLayout(vertical_layout)
        self.setCentralWidget(container)
        #self._create_status_bar()
    
    #def _create_status_bar(self):
       # status = QStatusBar()
        #status.showMessage(self._model.path)
       # self.setStatusBar(status)
 
class Model():
 
    def __init__(self):
        pass
 
    def _load_data(self):
 
        home_directory = str(Path.home())
        self._path = QFileDialog.getOpenFileName(self, 'Open file', home_directory,"Mp3 File (*.mp3)")[0]
        self.audiofile = eyed3.load(self._path)
        return self.audiofile
 
    def _save_tags_file(self):
        self.audiofile.tag.save()      
        
 
class Controller():
 
    def __init__(self, view, model):
        self._view=view
        self._model=model
        self._connect_signals()
    
    def _load_mp3_tags(self):
 
        self._model._load_data()
        self._view.artist = QLineEdit(self.audiofile.tag.artist)
        self._view.album = QLineEdit(self.audiofile.tag.album)
        self._view.song_num = QLineEdit(str(self.audiofile.tag.track_num[0]))
        self._view.cd_num = QLineEdit(str(self.audiofile.tag.track_num[1]))
        self._view.title = QLineEdit(self.audiofile.tag.title)
        self._view.genre= QLineEdit(str(self.audiofile.tag.genre))
        self._view.date= QLineEdit(str(self.audiofile.tag.original_release_date))
 
    
    def _update_tags(self):
 
        self.audiofile.tag.artist = self._view.artist.text()
        self.audiofile.tag.album = self._view.album.text()
        self.audiofile.tag.track_num = tuple([(str(self._view.song_num.text())), str((self._view.cd_num.text()))])
        self.audiofile.tag.title = self._view.title.text()
        self.audiofile.tag.genre= self._view.genre.text()
        self.audiofile.tag.original_release_date = (str(self._view.date.text()))
        self._model._save_tags_file()
 
 
    def _connect_signals(self):
       #self._view.button_exit.clicked.connect()
        self._view.button_save.clicked.connect(self._update_tags)
        self._view.button_open.clicked.connect(self._load_mp3_tags)
 
def main():
    mp3t = QApplication(sys.argv)
    view = View()
    model = Model()
    controller = Controller (view,model)
    
    view.show
    sys.exit(mp3t.exec())      
 

if __name__ == '__main__':
    main()