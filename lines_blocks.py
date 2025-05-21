from PyQt6 import QtWidgets
from styles import menu_lines_style


class TextLine(QtWidgets.QLineEdit):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(menu_lines_style)