from DBController.DBConnection import DBConnection


class SubjectInfoTable:
    def show(self):
        command = "SELECT * FROM subject_info;"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            subject_scores = cursor.fetchall()

        return subject_scores

    def insert(self, id, score_list):
        for subject, score in score_list.items():
            command = "INSERT INTO subject_info (stu_id, subject, score) VALUES  ('{}', '{}', '{}');".format(id, subject, score)

            with DBConnection() as connection:
                cursor = connection.cursor()
                cursor.execute(command)
                connection.commit()



    def select(self, id):
        command = "SELECT * FROM subject_info WHERE stu_id='{}';".format(id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return {row['subject'] : row['score'] for row in record_from_db}

    def delete(self, stu_id):
        command = "DELETE FROM subject_info WHERE stu_id='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update(self, stu_id, score_list):
        for subject, score in score_list.items():
            if self.search(stu_id, subject) != False:
                command = "UPDATE subject_info SET score='{}' WHERE stu_id='{}' AND subject='{}';".format(score, stu_id, subject)

                with DBConnection() as connection:
                    cursor = connection.cursor()
                    cursor.execute(command)
                    connection.commit()
            else:
                self.insert(stu_id, {subject : score})


    def search(self, id, subject):
        command = "SELECT * FROM subject_info WHERE stu_id='{}' AND subject='{}';".format(id, subject)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return False if len(record_from_db) == 0 else True