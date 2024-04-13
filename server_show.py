from StudentInfoProcessor import StudentInfoProcessor

class server_show():
    def __init__(self):
        self.student_dict = StudentInfoProcessor().read_student_file()
    def execute(self,data):
        sent_data={}
        sent_data['status'] = 'OK'
        sent_data['parameters']=self.student_dict
        return sent_data