import pickle

class StudentInfoProcessor:
    def __init__(self):
        #self.student_dict = dict()
        pass
    def read_student_file(self): 
        self.student_dict = dict()
        try:
            with open("student_dict.db", "rb") as fp:
                self.student_dict = pickle.load(fp)
        except:
            self.student_dict = {}
        return self.student_dict
    def restore_student_file(self,rs_student_dict): 
        with open("student_dict.db", "wb") as fp:
            pickle.dump(rs_student_dict, fp)