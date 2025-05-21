from PyQt6 import QtWidgets
from windows_and_button import VersionChoiceWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = VersionChoiceWindow()
    window.show()
    app.exec()