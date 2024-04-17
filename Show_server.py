from Student_Data import Student_Process


class Show_svr:
    def __init__(self):
        pass

    def execute(self, x):
        student_data = Student_Process().read_student_file()
        return {'status': 'OK', 'parameters': student_data}
