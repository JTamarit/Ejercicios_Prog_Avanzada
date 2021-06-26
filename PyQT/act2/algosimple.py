import sys

from PyQt6.QtGui import QImageReader, QTextLine
import eyed3


from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QDialogButtonBox
from PyQt6.QtWidgets import QFormLayout
from PyQt6.QtWidgets import QLineEdit, QLabel
from PyQt6.QtWidgets import QVBoxLayout
from eyed3.core import AudioFile

class Dialog(QDialog):
    filename= "music/Enter_Sandman.mp3"
    audiofile = eyed3.load(filename)

    author = audiofile.tag.artist 
    album = audiofile.tag.album 
    track_num = str(audiofile.tag.track_num)
    title = audiofile.tag.title
    track = audiofile.tag.track_num
    genre = str(audiofile.tag.genre)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('mp3 tag editor')
        dlg_layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow('Author:', QLineEdit(Dialog.author))
        form_layout.addRow('Album:', QLineEdit(Dialog.album))
        form_layout.addRow('Track num:', QLineEdit(Dialog.track_num))
        form_layout.addRow('Title:', QLineEdit(Dialog.title))
        form_layout.addRow('Genre:',QLineEdit(Dialog.genre))
        dlg_layout.addLayout(form_layout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        dlg_layout.addWidget(buttons)
        self.setLayout(dlg_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec())