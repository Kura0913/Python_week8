from StudentInfoProcessor import StudentInfoProcessor

class AddSrvStru():
    def __init__(self):
        pass

    def execute(parameters):
        stu_dict = StudentInfoProcessor().read_student_file()
        reply_msg = {'status':''}

        if parameters['name'] not in stu_dict.keys():
            stu_dict[parameters['name']] = parameters # if the name not in the stu_dict, add it
            # set "OK" status message if add success
            reply_msg['status'] = 'OK'
            reply_msg['parameters'] = parameters
        else:
            # set "Fail" status message if add failed
            reply_msg['status'] = 'Fail'
            reply_msg['reason'] = 'The name already exists.'

        # restore stu_dict to DB
        StudentInfoProcessor().restore_student_file(stu_dict)
        
        return reply_msg