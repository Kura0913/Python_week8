import pickle


class StudentInfoProcessor():
    def __init__(self):
        self.stu_dict = dict()
    # store stu_dict
    def restore_student_file(self, student_dict):
        # read DB file
        with open("student_dict.db", "wb") as fp:
            pickle.dump(student_dict, fp)
        print("Save success!!")


    def read_student_file(self):
        try:
            with open("student_dict.db", "rb") as fp:
                self.stu_dict = pickle.load(fp)
        except:
            pass

        return self.stu_dict