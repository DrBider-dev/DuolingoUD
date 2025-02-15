from typing import List
from Connections.MySql_Connection import MySQLDatabaseConnection
from Dao import ChallengesAchievementDAO


class ChallengesAchievement:
    
    """
    A class to manage CRUD operations for the ChallengesAchievement table in the database.
    Attributes:
        db_connection (DatabaseConnection): The database connection object.
    Methods:
        __init__(db_connection: DatabaseConnection):
            Initializes the ChallengesAchievement object with a database connection.
        create(data: ChallengesAchievementDAO) -> int:
            Inserts a new record into the ChallengesAchievement table.
        update(id_PK: int, data: ChallengesAchievementDAO):
            Updates an existing record in the ChallengesAchievement table.
        delete(id_PK: int):
            Deletes a record from the ChallengesAchievement table by its primary key.
        get_by_id(id_PK: int) -> ChallengesAchievementDAO:
            Retrieves a record from the ChallengesAchievement table by its primary key.
        get_all() -> List[ChallengesAchievementDAO]:
            Retrieves all records from the ChallengesAchievement table.
    """

    def __init__(self, db_connection: MySQLDatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: ChallengesAchievementDAO) -> int:
       
        query = """
            INSERT INTO ChallengesAchievement(Challlenges_FK, Achievement_FK)
            VALUES (%s, %s);
        """
        values = (data.Challenges_FK, data.Achievement_FK)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: ChallengesAchievementDAO):
      
        query = """
            UPDATE ChallengesAchievement
            SET Challlenges_FK = %s, Achievement_FK = %s
            WHERE id_PK = %s;
        """
        values = (data.Challenges_FK, data.Achievement_FK, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM ChallengesAchievement
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> ChallengesAchievementDAO:
       
        query = """
            SELECT id_PK, Challenges_FK, Achievement_FK 
            FROM ChallengesAchievement
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[ChallengesAchievementDAO]:
       
        query = """
            SELECT id_PK, Challenges_FK, Achievement_FK
            FROM ChallengesAchievement;
        """
        return self.db_connection.get_many(query)
