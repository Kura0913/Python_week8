from Student_Data import Student_Process


class Add_svr:
    def __init__(self):
        pass

    def execute(self, data):
        student_data = Student_Process().read_student_file()
        if len(data['scores']) == 0:
            return {'status': "Fail", 'reason': 'No Adding New Data'}

        if data['name'] in student_data:
            return {'status': "Fail", 'reason': "The name already exists."}

        # Add New Student Data
        student_data[data['name']] = data
        Student_Process().restore_data(student_data)
        return {'status': 'OK', 'parameters': {data['name']: data}}
