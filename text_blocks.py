from PyQt6 import QtWidgets
from styles import textedit_blocks_style


class MagazinesInputBlock(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(textedit_blocks_style)