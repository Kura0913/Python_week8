from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content, color="black"):
        super().__init__()
        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.setFont(QtGui.QFont("Arial", pointSize=font_size, weight=600))
        self.set_color(color)
        self.setText(content)

    def set_color(self, color):
        if color == 'red':
            self.setStyleSheet("color: red;")
        elif color == 'green':
            self.setStyleSheet(f"color: green;")
        else:
            self.setStyleSheet("color: black;")

class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=200, font_size=16, Number=False):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("Arial", font_size))
        if Number == True:
            validator = QtGui.QIntValidator(0, 999)
            self.setValidator(validator)

    def clear_editor_content(self, event):
        self.clear()

class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))

class ScrollAreaComponent(QtWidgets.QScrollArea):
    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.content = LabelComponent(16,"")

        container = QWidget()
        container.setLayout(QVBoxLayout())
        container.layout().addWidget(self.content)
        self.setWidget(container)