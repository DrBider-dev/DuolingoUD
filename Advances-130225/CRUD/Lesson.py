from typing import List
from Connections import DatabaseConnection
from Dao import LessonDAO


class Lesson:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: LessonDAO) -> int:
       
        query = """
            INSERT INTO Lesson(lesson_type, questions_FK, exp, time, accuracy)
            VALUES (%s, %s, %s, %s, %s);
        """
        values = (data.lesson_type, data.questions_FK, data.exp, data.time, data.accuracy)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: LessonDAO):
      
        query = """
            UPDATE Lesson
            SET lesson_type = %s, questions_FK = %s, exp = %s, time = %s, accuracy = %s
            WHERE id_PK = %s;
        """
        values = (data.lesson_type, data.questions_FK, data.exp, data.time, data.accuracy, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM Lesson
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> LessonDAO:
       
        query = """
            SELECT id_PK, lesson_type, questions_FK, exp, time, accuracy 
            FROM Lesson
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[LessonDAO]:
       
        query = """
            SELECT id_PK, lesson_type, questions_FK, exp, time, accuracy 
            FROM Lesson;
        """
        return self.db_connection.get_many(query)