from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class DelStu:
    def execute(self, parameters):
        SubjectInfoTable().delete(StudentInfoTable().select(parameters['name'])[0])
        StudentInfoTable().delete(StudentInfoTable().select(parameters['name'])[0])
        return {'status' : 'OK'}