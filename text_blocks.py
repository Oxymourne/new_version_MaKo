from PyQt6 import QtWidgets
from styles import textedit_blocks_style


class TextBlock(QtWidgets.QTextEdit):
    def __init__(self, text_input=False):
        super().__init__()

        self.setStyleSheet(textedit_blocks_style)
        self.setReadOnly(text_input)