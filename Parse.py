
from ServerShow import ServerShow
from ServerAdd import ServerAdd

action_list = {
    "add": ServerAdd,  
    "show": ServerShow
}

class Parse():
    def __init__(self):
        pass
    def execute(self,message):
        sent_data = action_list[message['command']]().execute(message['parameters'])
        return sent_data
    #將server收到的message取出cammand和parameters，透過action_list驅動對應command的function
 
