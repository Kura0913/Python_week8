import pickle


class Add_svr:
    def __init__(self):
        pass

    def execute(self, data):
        student_data = self.read_student_file()
        if data['name'] in student_data:
            return {'status': "Fail", 'reason': "The name already exists."}

        # Add New Student Data
        student_data[data['name']] = data
        self.restore_data(student_data)
        return {'status': 'OK', 'parameters': {data['name']: data}}

    def restore_data(self, data):
        with open("student_dict.db", "wb") as fp:
            pickle.dump(data, fp)

    def read_student_file(self):
        student_data = dict()
        try:
            with open("student_dict.db", "rb") as fp:
                student_data = pickle.load(fp)
        except:
            pass
        return student_data
