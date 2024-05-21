from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class PrintAll:
    def execute(self, parameters):
        student_name = StudentInfoTable().show()
        student_dict = {}
        for row in student_name:
            student_dict[row['name']] = {"name" : row['name'], 'scores' : SubjectInfoTable().select(row['stu_id'])}
        return {'status' : 'OK', 'parameters' : student_dict}
