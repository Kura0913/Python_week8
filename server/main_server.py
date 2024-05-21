from Commands.AddStu import AddStu
from Commands.DelStu import DelStu
from Commands.QueryStu import QueryStu
from Commands.PrintAll import PrintAll
from Commands.ModifyStu import ModifyStu
from SocketServer.SocketServer import SocketServer
from DBController.DBInitializer import DBInitializer
from DBController.DBConnection import DBConnection

action_list ={
    "add": AddStu,
    "show": PrintAll,
    "query": QueryStu,
    "delete" : DelStu,
    "modify" : ModifyStu
}

class JobDispatcher:
    def job_execute(self, command, parameters):
        execute_result = action_list[command]().execute(parameters)
        return execute_result

def main():
    DBConnection.db_file_path = "database.db"
    DBInitializer().execute()

    job_dispatcher = JobDispatcher()
    server = SocketServer(job_dispatcher)
    server.daemon = True
    server.serve()

    while True:
        command = input()
        if command == "finish":
            break

    server.server_socket.close()
    print("leaving .......")

main()
