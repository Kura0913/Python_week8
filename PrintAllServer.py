from StudentInfoProcessor import StudentInfoProcessor

class PrintAllServer:
    def __init__(self):
        pass

    def execute(self):
        student_dict = StudentInfoProcessor().read_student_file()
        reply_msg = dict()
        reply_msg['status'] = 'OK'
        reply_msg['parameters'] = student_dict
        return reply_msg
        
