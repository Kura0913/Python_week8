from StudentInfoProcessor import StudentInfoProcessor

class AddStuServer:
    def __init__(self):  
        pass                              

    def execute(new_stu_dict):
        student_dict = StudentInfoProcessor().read_student_file()
        reply_msg = dict()
        
        if new_stu_dict['name'] in student_dict:
            reply_msg['status'] = 'Fail'
            reply_msg['reason'] = 'The name already exists.'
        else:
            reply_msg['status'] = 'OK'
            reply_msg['parameters'] = new_stu_dict
            student_dict[new_stu_dict['name']] = new_stu_dict
            StudentInfoProcessor().restore_student_file(student_dict) 

        return reply_msg