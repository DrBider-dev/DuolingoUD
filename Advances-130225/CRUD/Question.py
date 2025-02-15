from typing import List
from Connections.MySql_Connection import MySQLDatabaseConnection
from Dao import QuestionDAO


class Question:

    """
    A class to represent CRUD operations for the Question table in the database.
    Attributes
    ----------
    db_connection : DatabaseConnection
        An instance of the DatabaseConnection class to interact with the database.
    Methods
    -------
    __init__(db_connection: DatabaseConnection):
        Initializes the Question instance with a database connection and connects to the database.
    create(data: QuestionDAO) -> int:
        Inserts a new question into the Question table and returns the ID of the created question.
    update(id_PK: int, data: QuestionDAO):
        Updates an existing question in the Question table based on the provided ID.
    delete(id_PK: int):
        Deletes a question from the Question table based on the provided ID.
    get_by_id(id_PK: int) -> QuestionDAO:
        Retrieves a question from the Question table based on the provided ID.
    get_all() -> List[QuestionDAO]:
        Retrieves all questions from the Question table.
    get_by_type(name: str) -> List[QuestionDAO]:
        Retrieves questions from the Question table based on the provided question type.
    """

    def __init__(self, db_connection: MySQLDatabaseConnection):
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
    
    def get_by_type(self, type: str) -> List[QuestionDAO]:
                    
        query = """
            SELECT id_PK, content, answer, isCorrect, question_type
            FROM Question
            WHERE question_type = %s;
        """
        values = (type,)
        return self.db_connection.get_many(query, values)