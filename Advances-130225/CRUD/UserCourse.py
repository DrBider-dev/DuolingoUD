from typing import List
from Connections import DatabaseConnection
from Dao import UserCourseDAO


class UserCourse:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: UserCourseDAO) -> int:
       
        query = """
            INSERT INTO UserCourse(User_FK, Course_FK)
            VALUES (%s, %s);
        """
        values = (data.User_FK, data.Course_FK)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: UserCourseDAO):
      
        query = """
            UPDATE UserCourse
            SET User_FK = %s, Course_FK = %s
            WHERE id_PK = %s;
        """
        values = (data.User_FK, data.Course_FK, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM UserCourse
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> UserCourseDAO:
       
        query = """
            SELECT id_PK, User_FK, Course_FK 
            FROM UserCourse
            WHERE id_PK = %s;
        """
        values = (id_PK)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[UserCourseDAO]:
       
        query = """
            SELECT id_PK, User_FK, Course_FK 
            FROM UserCourse;
        """
        return self.db_connection.get_many(query)