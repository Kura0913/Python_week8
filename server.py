from server_Show import ServerShow
from server_Add import ServerAddStu
from threading import Thread
from StudentDB import DB
import socket
import json

host = "127.0.0.1"
port = 20001

Func = {'add': ServerAddStu,
        'show': ServerShow}

class SocketServer(Thread):
    def __init__(self, host, port):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # The following setting is to avoid the server crash. So, the binded address can be reused
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.student_dict = DB().read_student_file()

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
                if message['command'] == "exit":
                    connection.send("closing".encode())
                    DB.restore_student_file(self.student_dict)
                    keep_going = False
                else:
                    print(f"{message}")
                    self.student_dict, reply_msg = parser(message, self.student_dict, address)
                    connection.send(json.dumps(reply_msg).encode())
        
        connection.close()
        print("\n{} close connection".format(address))

def parser(message,student_dict, address):
    print(f"    server recived:{message} from ({address})")
    if message['command'] == "add":
        ServerAddStu(student_dict).execute(message['parameters'])
    elif message['command'] == "show":
        ServerShow(student_dict).execute(message['parameters'])
    else:
        print("command error")
        return 0
    return student_dict, reply_msg

if __name__ == '__main__':
    server = SocketServer(host, port)
    server.daemon = True
    server.serve()

    # because we set daemon is true, so the main thread has to keep alive
    while True:
        command = input()
        if command == "finish":
            DB.restore_student_file(server.student_dict)
            break
    
    server.server_socket.close()
    print("leaving ....... ")
