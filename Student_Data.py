import pickle


class Student_Process:
    def __init__(self):
        pass

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
