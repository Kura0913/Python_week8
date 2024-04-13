from threading import Thread
from AddSrvStru import AddSrvStru
from PrintAllSrvStru import PrintAllSrvStru
import socket
import json

host = "127.0.0.1"
port = 20001

SRV_FUNC = {
    "add": AddSrvStru,
    "show": PrintAllSrvStru
}
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
            print(f"{address} connected")
            self.new_connection(connection=connection,
                                address=address)


    def new_connection(self, connection, address):
        Thread(target=self.receive_message_from_client,
               kwargs={
                   "connection": connection,
                   "address": address}, daemon=True).start()

    def receive_message_from_client(self, connection, address):
        # get students list        
        keep_going = True
        while keep_going:
            try:
                message = connection.recv(1024).strip().decode()
            except Exception as e:
                print(f"Exeption happened {e}, {address}")
                keep_going = False
            else:
                if not message:
                    keep_going = False
                message = json.loads(message)
                if message['command'] == "exit":
                    connection.send("closing".encode())
                    keep_going = False
                else:
                    print(f'    The server recived data =>{message}')
                    reply_msg = SRV_FUNC[message['command']].execute(message['parameters'])
                    print(f'    The server send adata =>{reply_msg}')
                    connection.send(json.dumps(reply_msg).encode())
        
        connection.close()
        print(f"{address} close connection")


if __name__ == '__main__':
    server = SocketServer(host, port)
    server.daemon = True
    server.serve()

    # because we set daemon is true, so the main thread has to keep alive
    print(f'Server start...')
    print('====================')
    while True:
        command = input()
        if command == "finish":
            break
    
    server.server_socket.close()
    print("leaving ....... ")