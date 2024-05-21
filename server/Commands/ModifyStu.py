from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class ModifyStu:
    def execute(self, parameters):
        SubjectInfoTable().update(StudentInfoTable().select(parameters['name'])[0],parameters['scores_dict'])
        return {'status' : 'OK'}