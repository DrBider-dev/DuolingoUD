from typing import List
from Connections import DatabaseConnection
from Dao import UserQuestionDAO


class UserQuestion:
    
    """
    A class used to represent the UserQuestion entity and perform CRUD operations on it.
    Attributes
    ----------
    db_connection : DatabaseConnection
        An instance of the DatabaseConnection class to interact with the database.
    Methods
    -------
    __init__(db_connection: DatabaseConnection)
        Initializes the UserQuestion instance with a database connection and connects to the database.
    create(data: UserQuestionDAO) -> int
        Inserts a new UserQuestion record into the database and returns the ID of the created record.
    update(id_PK: int, data: UserQuestionDAO)
        Updates an existing UserQuestion record in the database based on the provided ID.
    delete(id_PK: int)
        Deletes a UserQuestion record from the database based on the provided ID.
    get_by_id(id_PK: int) -> UserQuestionDAO
        Retrieves a UserQuestion record from the database based on the provided ID.
    get_all() -> List[UserQuestionDAO]
        Retrieves all UserQuestion records from the database.
    """

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