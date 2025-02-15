from typing import List
from Connections.MySql_Connection import MySQLDatabaseConnection
from Dao import ChallengesDAO


class Challenges:
    
    """
    A class to represent the CRUD operations for Challenges.
    Attributes
    ----------
    db_connection : DatabaseConnection
        An instance of the DatabaseConnection class to interact with the database.
    Methods
    -------
    __init__(db_connection: DatabaseConnection)
        Initializes the Challenges class with a database connection.
    create(data: ChallengesDAO) -> int
        Inserts a new challenge into the database and returns the ID of the created challenge.
    update(id_PK: int, data: ChallengesDAO)
        Updates an existing challenge in the database based on the provided ID.
    delete(id_PK: int)
        Deletes a challenge from the database based on the provided ID.
    get_by_id(id_PK: int) -> ChallengesDAO
        Retrieves a challenge from the database based on the provided ID.
    get_all() -> List[ChallengesDAO]
        Retrieves all challenges from the database.
    """


    def __init__(self, db_connection: MySQLDatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: ChallengesDAO) -> int:
       
        query = """
            INSERT INTO Challenges(description, progress, goal, reward)
            VALUES (%s, %s, %s, %s);
        """
        values = (data.description, data.progress, data.goal, data.reward)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: ChallengesDAO):
      
        query = """
            UPDATE Challenges
            SET description = %s, progress = %s, goal = %s, reward = %s
            WHERE id_PK = %s;
        """
        values = (data.description, data.progress, data.goal, data.reward, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
        
            query = """
                DELETE FROM Challenges
                WHERE id_PK = %s;
            """
            self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> ChallengesDAO:
       
        query = """
            SELECT id_PK, description, progress, goal, reward 
            FROM Challenges
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[ChallengesDAO]:
       
        query = """
            SELECT id_PK, description, progress, goal, reward 
            FROM Challenges;
        """
        return self.db_connection.get_many(query)