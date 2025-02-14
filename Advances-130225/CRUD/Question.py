from typing import List
from Connections import DatabaseConnection
from Dao import QuestionDAO


class Question:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: QuestionDAO) -> int:
       
        query = """
            INSERT INTO Question(content, answer, isCorrect, question_type)
            VALUES (%s, %s, %s, %s);
        """
        values = (data.name, data.progressPercentage, data.goal)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: QuestionDAO):
      
        query = """
            UPDATE Question
            SET content = %s, answer = %s, isCorrect = %s, question_type = %s
            WHERE id_PK = %s;
        """
        values = (data.name, data.progressPercentage, data.goal, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
        
            query = """
                DELETE FROM Question
                WHERE id_PK = %s;
            """
            values = (id_PK,)
            self.db_connection.delete(query, values)

    def get_by_id(self, id_PK: int) -> QuestionDAO:
       
        query = """
            SELECT id_PK, content, answer, isCorrect, question_type 
            FROM Question
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[QuestionDAO]:
       
        query = """
            SELECT id_PK, content, answer, isCorrect, question_type
            FROM Question;
        """
        return self.db_connection.get_many(query)
    
    def get_by_type(self, name: str) -> List[QuestionDAO]:
                    
        query = """
            SELECT id_PK, content, answer, isCorrect, question_type
            FROM Question
            WHERE question_type = %s;
        """
        values = (name,)
        return self.db_connection.get_many(query, values)