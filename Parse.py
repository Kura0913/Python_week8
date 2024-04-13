
from server_show import server_show
from server_add import server_add

action_list = {
    "add": server_add,  
    "show": server_show
}

class Parse():
    def __init__(self):
        pass
    def execute(self,message):
        sent_data = action_list[message['command']]().execute(message['parameters'])
        return sent_data
 
