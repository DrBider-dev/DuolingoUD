from typing import List
from Connections import DatabaseConnection
from Dao import CourseDAO


class Course:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: CourseDAO) -> int:
         
          query = """
                INSERT INTO Course(language, stages_FK)
                VALUES (%s, %s);
          """
          values = (data.language, data.stages_FK)
          return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: CourseDAO):
      
        query = """
            UPDATE Course
            SET language = %s, stages_FK = %s
            WHERE id_PK = %s;
        """
        values = (data.language, data.stages_FK, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM Course
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> CourseDAO:
       
        query = """
            SELECT id_PK, language, stages_FK 
            FROM Course
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)
    
    def get_all(self) -> List[CourseDAO]:
       
        query = """
            SELECT id_PK, language, stages_FK 
            FROM Course;
        """
        return self.db_connection.get_many(query)

    def get_by_language(self, language: str) -> List[CourseDAO]:
   
        query = """
            SELECT id_PK, language, stages_FK 
            FROM Course;
            WHERE LOWER(language) LIKE LOWER(%s);
        """
        values = (f'%{language}%',)
        return self.db_connection.get_many(query, values)