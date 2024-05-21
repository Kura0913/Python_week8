from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
from SocketClient import SocketClient
import json

class ServiceController:
    def command_sender(self, socket_client, command, data):
        socket_client.send_command(command, data)
        result = socket_client.wait_response()
        return result

class ExecuteConfirmCommand(QtCore.QThread):
    result_msg = pyqtSignal(str)
    def __init__(self, socket_client, command, parameters=dict()):
        super().__init__()
        self.socket_client = socket_client
        self.command = command
        self.parameters = parameters

    def run(self):
        result = ServiceController().command_sender(self.socket_client, self.command, self.parameters)
        self.result_msg.emit(json.dumps(result))