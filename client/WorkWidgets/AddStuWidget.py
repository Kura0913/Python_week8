from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from SocketClient.ServiceController import ExecuteConfirmCommand
import json


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self, socket_client):
        super().__init__()
        self.setObjectName("add_stu_widget")
        self.socket_client = socket_client
        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Add Student")
        self.name_label = LabelComponent(16, "Name: ")
        self.subject_label = LabelComponent(16, "Subject: ")
        self.score_label = LabelComponent(16, "Score: ")
        self.message_label = LabelComponent(12, "", "red")
        self.name_editor = LineEditComponent("Name")
        self.subject_editor = LineEditComponent("Subject")
        self.score_editor = LineEditComponent("", Number=True)
        self.Querybutton = ButtonComponent("Query")
        self.Addbutton = ButtonComponent("Add")
        self.Sendbutton = ButtonComponent("Send")

        self.Querybutton.clicked.connect(self.click_query)
        self.Addbutton.clicked.connect(self.click_add)
        self.Sendbutton.clicked.connect(self.click_send)

        self.name_editor.textChanged.connect(self.query_situation)
        self.subject_editor.textChanged.connect(self.add_situation)
        self.score_editor.textChanged.connect(self.add_situation)

        self.name_editor.mousePressEvent = self.name_editor.clear_editor_content
        self.subject_editor.mousePressEvent = self.subject_editor.clear_editor_content
        self.score_editor.mousePressEvent = self.score_editor.clear_editor_content

        layout.addWidget(header_label, 0, 0, 1, 2)
        layout.addWidget(self.name_label, 1, 0, 1, 1)
        layout.addWidget(self.subject_label, 2, 0, 1, 1)
        layout.addWidget(self.score_label, 3, 0, 1, 1)
        layout.addWidget(self.message_label, 1, 3 , 4, 1)
        layout.addWidget(self.name_editor, 1, 1, 1, 1)
        layout.addWidget(self.subject_editor, 2, 1, 1, 1)
        layout.addWidget(self.score_editor, 3, 1, 1, 1)
        layout.addWidget(self.Querybutton, 1, 2, 1, 1)
        layout.addWidget(self.Addbutton, 3, 2, 1, 1)
        layout.addWidget(self.Sendbutton, 5, 3, 1, 1)

        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 3)
        layout.setColumnStretch(3, 5)
        layout.setRowStretch(0, 3)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 5)
        layout.setRowStretch(5, 2)

        self.setLayout(layout)
        self.reset()

    def load(self):
        print("<<< add widget >>>")
        self.reset()

    def click_query(self):
        if self.name_editor.text() == "":
            self.set_message("Name editor can't be empty", "red", True)
        else:
            self.execution = ExecuteConfirmCommand(self.socket_client, "query", {"name" : self.name_editor.text()})
            self.execution.start()
            self.execution.result_msg.connect(self.action_query)

    def action_query(self, result):
        result = json.loads(result)
        if result["status"] == "Fail":
            self.subject_editor.setEnabled(True)
            self.score_editor.setEnabled(True)
            self.name_editor.setEnabled(False)
            self.Querybutton.setEnabled(False)
            self.set_message(f"Query Success, Please enter subjects for student {self.name_editor.text()}", "green")
        else:
            self.set_message("Query Fail, Name is already taken", "red", True)

    def click_add(self):
        if self.subject_editor.text() == "" or self.score_editor.text() == "" or self.subject_editor.text() == "Subject":
            self.set_message("Subject or Score editor can't be empty, Please refill it", "red")
        else:
            if self.subject_editor.text() not in self.add_scorelist:
                self.add_scorelist[self.subject_editor.text()] = self.score_editor.text()
                self.set_message(f"Student {self.name_editor.text()}'s subject '{self.subject_editor.text()}' with score '{self.score_editor.text()}' added", "green")
                self.Sendbutton.setEnabled(True)
            else:
                self.set_message(f"The {self.name_editor.text()}'s subject '{self.subject_editor.text()}' is already exist", "red")
            self.subject_editor.setText("Subject")
            self.score_editor.setText("")

    def click_send(self):
        self.score_info = {"name":self.name_editor.text(), "scores":self.add_scorelist}
        self.execution = ExecuteConfirmCommand(self.socket_client, "add", self.score_info)
        self.execution.start()
        self.execution.result_msg.connect(self.action_send)

    def action_send(self, result):
        result = json.loads(result)
        self.message_label.set_color("green")
        self.message_label.setText(f"Send Success ...\nAdd {self.score_info} successfully")
        QtCore.QTimer.singleShot(3000, self.reset)

    def set_message(self, text, color, setReset=False):
        self.message_label.set_color(color)
        self.message_label.setText(text)
        if setReset:
            QtCore.QTimer.singleShot(2000, self.reset)

    def reset(self):
        self.add_scorelist = dict()
        self.name_editor.setEnabled(True)
        self.Addbutton.setEnabled(False)
        self.Sendbutton.setEnabled(False)
        self.subject_editor.setEnabled(False)
        self.score_editor.setEnabled(False)
        self.Querybutton.setEnabled(False)

        self.name_editor.setText("Name")
        self.subject_editor.setText("Subject")
        self.score_editor.setText("")
        self.message_label.setText("")
        self.message_label.set_color("red")

    def query_situation(self):
        if self.name_editor.text() == "":
            self.Querybutton.setEnabled(False)
        else:
            self.Querybutton.setEnabled(True)

    def add_situation(self):
        if self.subject_editor.text() == "" or self.score_editor.text() == "":
            self.Addbutton.setEnabled(False)
        else:
            self.Addbutton.setEnabled(True)
