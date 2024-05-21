from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class AddStu:
    def execute(self,parameters):
        StudentInfoTable().insert(parameters['name'])
        SubjectInfoTable().insert(StudentInfoTable().select(parameters['name'])[0], parameters['scores'])
        return {'status' : 'OK'}