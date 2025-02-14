from typing import List
from Connections import DatabaseConnection
from Dao import UserQuestionDAO


class UserQuestion:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: UserQuestionDAO) -> int:
       
        query = """
            INSERT INTO UserQuestion(User_FK, Question_FK)
            VALUES (%s, %s);
        """
        values = (data.User_FK, data.Question_FK)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: UserQuestionDAO):
      
        query = """
            UPDATE UserQuestion
            SET User_FK = %s, Question_FK = %s
            WHERE id_PK = %s;
        """
        values = (data.User_FK, data.Question_FK, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM UserQuestion
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> UserQuestionDAO:
       
        query = """
            SELECT id_PK, User_FK, Question_FK 
            FROM UserQuestion
            WHERE id_PK = %s;
        """
        values = (id_PK)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[UserQuestionDAO]:
       
        query = """
            SELECT id_PK, User_FK, Question_FK 
            FROM UserQuestion;
        """
        return self.db_connection.get_many(query)