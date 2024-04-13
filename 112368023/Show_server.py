import pickle


class Show_svr:
    def __init__(self):
        pass

    def execute(self, x):
        student_data = self.read_student_file()
        return {'status': 'OK', 'parameters': student_data}

    def read_student_file(self):
        student_data = dict()
        try:
            with open("student_dict.db", "rb") as fp:
                student_data = pickle.load(fp)
        except:
            pass
        return student_data
