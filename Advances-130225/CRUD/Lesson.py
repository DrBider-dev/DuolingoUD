from typing import List
from Connections import DatabaseConnection
from Dao import LessonDAO


class Lesson:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: LessonDAO) -> int:
       
        query = """
            INSERT INTO Lesson(name, progressPercentage, goal)
            VALUES (%s, %s, %s);
        """
        values = (data.name, data.progressPercentage, data.goal)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: LessonDAO):
      
        query = """
            UPDATE Lesson
            SET name = %s, progressPercentage = %s, goal = %s
            WHERE id_PK = %s;
        """
        values = (data.name, data.progressPercentage, data.goal, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM Lesson
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> LessonDAO:
       
        query = """
            SELECT id_PK, name, progressPercentage, goal 
            FROM Lesson
            WHERE id_PK = %s;
        """
        values = (id_PK)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[LessonDAO]:
       
        query = """
            SELECT id_PK, name, progressPercentage, goal 
            FROM Lesson;
        """
        return self.db_connection.get_many(query)

    def get_by_name(self, name: str) -> List[LessonDAO]:
   
        query = """
            SELECT id_PK, name, progressPercentage, goal 
            FROM Lesson
            WHERE LOWER(name) LIKE LOWER(%s);
        """
        values = (f'%{name}%',)
        return self.db_connection.get_many(query, values)