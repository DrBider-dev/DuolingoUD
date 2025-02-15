from typing import List
from Connections.MySql_Connection import MySQLDatabaseConnection
from Dao import ChallengesBoostersDAO


class ChallengesBoosters:
    """
    A class used to represent the ChallengesBoosters operations.
    ...
    Attributes
    ----------
    db_connection : DatabaseConnection
        a database connection object to interact with the database
    Methods
    -------
    __init__(db_connection: DatabaseConnection)
        Initializes the ChallengesBoosters with a database connection.
    create(data: ChallengesBoostersDAO) -> int
        Inserts a new record into the ChallengesBoosters table.
    update(id_PK: int, data: ChallengesBoostersDAO)
        Updates an existing record in the ChallengesBoosters table.
    delete(id_PK: int)
        Deletes a record from the ChallengesBoosters table by its primary key.
    get_by_id(id_PK: int) -> ChallengesBoostersDAO
        Retrieves a record from the ChallengesBoosters table by its primary key.
    get_all() -> List[ChallengesBoostersDAO]
        Retrieves all records from the ChallengesBoosters table.
    """

    def __init__(self, db_connection: MySQLDatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: ChallengesBoostersDAO) -> int:
       
        query = """
            INSERT INTO ChallengesBoosters(Challlenges_FK, Boosters_FK)
            VALUES (%s, %s);
        """
        values = (data.Challenges_FK, data.Boosters_FK)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: ChallengesBoostersDAO):
      
        query = """
            UPDATE ChallengesBoosters
            SET Challlenges_FK = %s, Boosters_FK = %s
            WHERE id_PK = %s;
        """
        values = (data.Challenges_FK, data.Boosters_FK, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM ChallengesBoosters
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> ChallengesBoostersDAO:
       
        query = """
            SELECT id_PK, Challenges_FK, Boosters_FK 
            FROM ChallengesBoosters
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[ChallengesBoostersDAO]:
       
        query = """
            SELECT id_PK, Challenges_FK, Boosters_FK
            FROM ChallengesBoosters;
        """
        return self.db_connection.get_many(query)
