from StudentInfoProcessor import StudentInfoProcessor

class PrintAllSrvStru():
    def __init__(self):
        pass

    def execute(parameters):
        stu_dict = StudentInfoProcessor().read_student_file()
        reply_msg = {'status':''}

        if stu_dict != None:
            reply_msg['status'] = 'OK'
            reply_msg['parameters'] = stu_dict
        else:
            reply_msg['status'] = 'Fail'
            reply_msg['reason'] = 'Get students list fail.'
        
        return reply_msg