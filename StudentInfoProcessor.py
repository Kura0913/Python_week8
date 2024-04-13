import pickle

class StudentInfoProcessor:
    def __init__(self):
        self.student_dict = dict()

    def read_student_file(self):
        try:
            with open("student_dict.db", "rb") as fp:
                self.student_dict = pickle.load(fp)
        except:
            pass

        return self.student_dict

    def restore_student_file(self, student_dict):
        with open("student_dict.db", "wb") as fp:
            pickle.dump(student_dict, fp)