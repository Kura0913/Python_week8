from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.ShowStuWidget import ShowStuWidget
from WorkWidgets.WidgetComponents import LabelComponent
from WorkWidgets.WidgetComponents import ButtonComponent
from SocketClient.SocketClient import SocketClient

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")

        layout = QtWidgets.QGridLayout()
        header_label = LabelComponent(24, "Student Management System")
        function_widget = FunctionWidget()
        menu_widget = MenuWidget(function_widget.update_widget)

        layout.addWidget(header_label, 0, 0, 1, 2)
        layout.addWidget(menu_widget, 1, 0, 1, 1)
        layout.addWidget(function_widget, 1, 1, 2, 2)

        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 8)
        layout.setColumnStretch(2, 2)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 6)

        self.setLayout(layout)

class MenuWidget(QtWidgets.QWidget):
    def __init__(self, update_widget_callback):
        super().__init__()
        self.setObjectName("menu_widget")
        self.update_widget_callback = update_widget_callback

        layout = QtWidgets.QVBoxLayout()
        self.add_button = ButtonComponent("Add student")
        self.show_button = ButtonComponent("Show all")
        self.add_button.clicked.connect(lambda: self.update_widget_callback("add"))
        self.show_button.clicked.connect(lambda: self.update_widget_callback("show"))

        layout.addWidget(self.add_button, stretch=1)
        layout.addWidget(self.show_button, stretch=1)
        self.setLayout(layout)

class FunctionWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.socket_client = SocketClient()
        self.widget_dict = {
            "add": self.addWidget(AddStuWidget(self.socket_client)),
            "show": self.addWidget(ShowStuWidget(self.socket_client))
        }
        self.update_widget("add")
    
    def update_widget(self, name):
        self.setCurrentIndex(self.widget_dict[name])
        current_widget = self.currentWidget()
        current_widget.load()
