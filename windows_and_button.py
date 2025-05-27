from core import *
from PyQt6.QtCore import Qt, pyqtSignal
from labels import *
from lines_blocks import TextLine
from styles import button_style, main_window_style, check_box_style
from text_blocks import TextBlock
from exceptions import *


class VersionChoiceWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 150)
        self.setStyleSheet("background-color: #F4F7F9;")

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        layout = QtWidgets.QGridLayout(central_widget)

        self.auto_version_window = AutoVersionWindow()
        self.custom_version_window = CustomVersionWindow()

        button_default = Button('Генерация кодов')
        layout.addWidget(button_default, 1, 0)
        button_default.clicked.connect(self.show_auto_version_window)

        button_custom = Button('Ручная настройка кодов')
        layout.addWidget(button_custom, 1, 1)
        button_custom.clicked.connect(self.show_custom_version_window)

        layout.addWidget(ChoiceWindowLabel('Выбери версию приложения'),
                         0, 0, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignCenter)

    def show_auto_version_window(self):
        self.close()
        self.auto_version_window.show()

    def show_custom_version_window(self):
        self.close()
        self.custom_version_window.show()


class Button(QtWidgets.QPushButton):
    def __init__(self, text):
        super().__init__()

        self.setFixedHeight(40)
        self.setText(text)
        self.setStyleSheet(button_style)


class AutoVersionWindow(QtWidgets.QMainWindow):
    api_data_signal = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 600)
        self.setWindowTitle('MaKo V2.0 Автоматический режим')
        self.setStyleSheet(main_window_style)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QGridLayout(central_widget)

        layout.addWidget(MenuLabel('Названия точек'), 0, 0)
        self.magazines_titles = TextBlock()
        layout.addWidget(self.magazines_titles, 1, 0, 6, 1)

        self.version_button = Button('Сменить версию')
        layout.addWidget(self.version_button, 7, 0)
        self.version_button.clicked.connect(self.switch_version)

        layout.addWidget(MenuLabel('Api ключ *'),
                         0, 1,
                         alignment=Qt.AlignmentFlag.AlignVCenter)
        self.api_text_line = TextLine()
        layout.addWidget(self.api_text_line, 0, 2)

        layout.addWidget(MenuLabel('Название бренда *'),
                         1, 1,
                         alignment=Qt.AlignmentFlag.AlignVCenter)
        self.brand_name = TextLine()
        layout.addWidget(self.brand_name, 1, 2)

        layout.addWidget(MenuLabel('Порт для Waiter'),
                         2, 1,
                         alignment=Qt.AlignmentFlag.AlignVCenter)
        self.waiter_line = TextLine()
        self.waiter_line.setFixedWidth(100)
        layout.addWidget(self.waiter_line, 2, 2)

        layout.addWidget(MenuLabel('Начальный код точек *'),
                         3, 1,
                         alignment=Qt.AlignmentFlag.AlignVCenter)
        self.magazines_codes = TextLine()
        self.magazines_codes.setFixedWidth(50)
        layout.addWidget(self.magazines_codes, 3, 2)

        layout.addWidget(MenuLabel('Списание по СМС'),
                         4, 1,
                         alignment=Qt.AlignmentFlag.AlignVCenter)
        self.sms_check = SmsCheckBox()
        layout.addWidget(self.sms_check, 4, 2)

        self.make_plugins_button = Button('Сделать плагины')
        layout.addWidget(self.make_plugins_button, 7, 2)
        self.make_plugins_button.clicked.connect(self.get_input_values)

        layout.addWidget(MenuLabel('ОШИБКИ'),
                         5, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignHCenter)
        self.errors_field = TextBlock(text_input=True)
        layout.addWidget(self.errors_field, 6, 1, 1, 2)

    def get_input_values(self):

        self.errors_field.clear()

        try:
            titles_data = correct_stores_list(self.magazines_titles.toPlainText())
        except MyError as e:
            self.errors_field.append(f'Названия точек: {e}')
        else:
            try:
                api_data = correct_api(self.api_text_line.text())
            except MyError as e:
                self.errors_field.append(f'Api ключ: {e}')
            else:
                try:
                    brand_name = correct_brand(self.brand_name.text())
                except MyError as e:
                    self.errors_field.append(f'Название бренда: {e}')
                else:
                    try:
                        codes_data = correct_shop_code(self.magazines_codes.text())
                    except MyError as e:
                        self.errors_field.append(f'Начальный код точек: {e}')
                    else:
                        port_data = self.waiter_line.text()
                        check_sms = self.sms_check.isChecked()

                        input_data = (titles_data, api_data, brand_name, port_data, codes_data, check_sms)
                        self.api_data_signal.emit(input_data)
                        main_function(*input_data)

    def switch_version(self):
        self.close()
        self.custom_version_window = CustomVersionWindow()
        self.custom_version_window.show()


class SmsCheckBox(QtWidgets.QCheckBox):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(check_box_style)


class CustomVersionWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 600)
        self.setWindowTitle('MaKo V2.0 Кастомный режим')
        self.setStyleSheet(main_window_style)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QGridLayout(central_widget)

        layout.addWidget(MenuLabel('Названия точек'), 0, 0)
        self.magazines_titles = TextBlock()
        layout.addWidget(self.magazines_titles, 1, 0, 4, 1)

        layout.addWidget(MenuLabel('Коды точек'),
                         5, 0)
        self.magazines_codes = TextBlock()
        layout.addWidget(self.magazines_codes, 6, 0, 1, 1)

        self.version_button = Button('Сменить версию')
        layout.addWidget(self.version_button, 7, 0)
        self.version_button.clicked.connect(self.switch_version)

        layout.addWidget(MenuLabel('Api ключ *'),
                         0, 1,
                         alignment=Qt.AlignmentFlag.AlignVCenter)
        self.api_text_line = TextLine()
        layout.addWidget(self.api_text_line, 0, 2)

        layout.addWidget(MenuLabel('Название бренда *'),
                         1, 1,
                         alignment=Qt.AlignmentFlag.AlignVCenter)
        self.brand_name = TextLine()
        layout.addWidget(self.brand_name, 1, 2)

        layout.addWidget(MenuLabel('Порт для Waiter'),
                         2, 1,
                         alignment=Qt.AlignmentFlag.AlignVCenter)
        self.waiter_line = TextLine()
        self.waiter_line.setFixedWidth(100)
        layout.addWidget(self.waiter_line, 2, 2)

        layout.addWidget(MenuLabel('Списание по СМС'),
                         3, 1,
                         alignment=Qt.AlignmentFlag.AlignVCenter)
        self.sms_check = SmsCheckBox()
        layout.addWidget(self.sms_check, 3, 2)

        self.make_plugins_button = Button('Сделать плагины')
        layout.addWidget(self.make_plugins_button, 7, 2)
        self.make_plugins_button.clicked.connect(self.get_input_values)

        layout.addWidget(MenuLabel('ОШИБКИ'),
                         5, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignHCenter)
        self.errors_field = TextBlock(text_input=True)
        layout.addWidget(self.errors_field, 6, 1, 1, 2)

    def get_input_values(self):
        a = self.api_text_line.text()

    def switch_version(self):
        self.close()
        self.auto_version_window = AutoVersionWindow()
        self.auto_version_window.show()


def aaa(text):
    print(f'Вот мои значния: {text}')
