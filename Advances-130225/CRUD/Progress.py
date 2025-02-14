from typing import List
from Connections import DatabaseConnection
from Dao import ProgressDAO


class Progress:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: ProgressDAO) -> int:
       
        query = """
            INSERT INTO Progress(course_FK, user_FK, streakDays, dailyExp, weeklyExp, totalExp, percentage)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        values = (data.course_FK, data.user_FK, data.streakDays, data.dailyExp, data.weeklyExp, data.totalExp, data.percentage)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: ProgressDAO):
      
        query = """
            UPDATE Progress
            SET course_FK = %s, user_FK = %s, streakDays = %s, dailyExp = %s, weeklyExp = %s, totalExp = %s, percentage = %s
            WHERE id_PK = %s;
        """
        values = (data.course_FK, data.user_FK, data.streakDays, data.dailyExp, data.weeklyExp, data.totalExp, data.percentage, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM Progress
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        self.db_connection.delete(query, values)

    def get_by_id(self, id_PK: int) -> ProgressDAO:
       
        query = """
            SELECT id_PK, course_FK, user_FK, streakDays, dailyExp, weeklyExp, totalExp, percentage
            FROM Progress
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)