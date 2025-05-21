from PyQt6 import QtWidgets
from styles import menu_labels_style, choice_labels_style


class MenuLabel(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__()

        self.setText(text)
        self.setStyleSheet(menu_labels_style)

class ChoiceWindowLabel(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__()

        self.setText(text)
        self.setStyleSheet(choice_labels_style)




