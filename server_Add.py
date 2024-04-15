class ServerAddStu:
    def __init__(self,student_dict):
        self.student_dict = student_dict

    def execute(self,addlist):
        if addlist['name'] in self.student_dict:
            return self.student_dict, {'status' : 'Fail', 'reason': 'The name already exists.'}
        else:
            self.student_dict[addlist['name']] = addlist
            return self.student_dict, {'status' : 'OK'}