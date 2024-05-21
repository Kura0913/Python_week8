from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable
class QueryStu:
    def execute(self,parameters):
        if len(StudentInfoTable().select(parameters['name'])) == 0:
            return {'status' : 'Fail','parameters' : 'The name is not found.'}
        return {'status' : 'OK','scores' : SubjectInfoTable().select(StudentInfoTable().select(parameters['name'])[0])}