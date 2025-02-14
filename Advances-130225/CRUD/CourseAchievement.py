from typing import List
from Connections import DatabaseConnection
from Dao import CourseAchievementDAO


class CourseAchievement:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: CourseAchievementDAO) -> int:
       
        query = """
            INSERT INTO CourseAchievement(Course_FK, Achievement_FK)
            VALUES (%s, %s);
        """
        values = (data.Course_FK, data.Achievement_FK)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: CourseAchievementDAO):
      
        query = """
            UPDATE CourseAchievement
            SET Course_FK = %s, Achievement_FK = %s
            WHERE id_PK = %s;
        """
        values = (data.Course_FK, data.Achievement_FK, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM CourseAchievement
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> CourseAchievementDAO:
       
        query = """
            SELECT id_PK, Course_FK, Achievement_FK 
            FROM CourseAchievement
            WHERE id_PK = %s;
        """
        values = (id_PK)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[CourseAchievementDAO]:
       
        query = """
            SELECT id_PK, Course_FK, Achievement_FK 
            FROM CourseAchievement;
        """
        return self.db_connection.get_many(query)