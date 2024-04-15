class ServerShow:
    def __init__(self,student_dict):
        self.student_dict = student_dict

    def execute(self, parameters):
            return self.student_dict, {'status' : 'OK','parameters' : self.student_dict}