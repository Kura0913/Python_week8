from DBController.DBConnection import DBConnection


class StudentInfoTable:
    def show(self):
        command = "SELECT * FROM student_info;"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            student_name = cursor.fetchall()

        return student_name

    def insert(self, name):
        command = "INSERT INTO student_info (name) VALUES  ('{}');".format(name)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def select(self, name):
        command = "SELECT * FROM student_info WHERE name='{}';".format(name)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['stu_id'] for row in record_from_db]

    def delete(self, stu_id):
        command = "DELETE FROM student_info WHERE stu_id='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update(self, stu_id, name):
        command = "UPDATE student_info SET name='{}' WHERE stu_id='{}';".format(name, stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
       