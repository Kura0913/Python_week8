from threading import Thread
import socket
import json
from Add_server import Add_svr
from Show_server import Show_svr


function_list = {'add': Add_svr,
                 'show': Show_svr}


class SocketServer(Thread):
    def __init__(self, host, port):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # The following setting is to avoid the server crash. So, the binded address can be reused
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)

    def serve(self):
        self.start()

    def run(self):
        while True:
            connection, address = self.server_socket.accept()
            print("{} connected".format(address))
            self.new_connection(connection=connection,
                                address=address)

    def new_connection(self, connection, address):
        Thread(target=self.receive_message_from_client,
               kwargs={
                   "connection": connection,
                   "address": address}, daemon=True).start()

    def receive_message_from_client(self, connection, address):
        keep_going = True
        while keep_going:
            try:
                message = connection.recv(1024).strip().decode()
            except Exception as e:
                print("Exeption happened {}, {}".format(e, address))
                keep_going = False
            else:
                if not message:
                    keep_going = False
                message = json.loads(message)
                if message['command'] == "close":
                    connection.send("closing".encode())
                    keep_going = False
                else:
                    print(message, address)
                    reply_msg = Receive_Client(message, address)
                    connection.send(json.dumps(reply_msg).encode())

        connection.close()
        print("{} close connection".format(address))


def Receive_Client(message, address):
    receive_command = message['command']
    parameters = message['parameters']
    print(f'    server received:{message} from:{address}')
    data = function_list[receive_command]().execute(parameters)
    return data


if __name__ == '__main__':
    Server = SocketServer('127.0.0.1', 20001)
    Server.daemon = True
    Server.serve()

    while True:
        command = input()
        if command == 'finish':
            break
    Server.server_socket.close()
    print("Server Close")
