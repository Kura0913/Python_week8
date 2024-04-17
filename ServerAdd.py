from StudentInfoProcessor import StudentInfoProcessor

class ServerAdd():
    def __init__(self):
        self.student_dict = StudentInfoProcessor().read_student_file()#讀取database
    def execute(self,data):
        sent_data={}
        if data['name'] in self.student_dict:#如果收到的
            sent_data['status'] = 'Fail'
            sent_data['reason']='The name already exists.'
        else:
            self.student_dict[data['name']]=data
            StudentInfoProcessor().restore_student_file(self.student_dict)
            sent_data['status'] = 'OK'
        
        return sent_data       
