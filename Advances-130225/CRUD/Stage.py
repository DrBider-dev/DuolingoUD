from typing import List
from Connections.MySql_Connection import MySQLDatabaseConnection
from Dao import StageDAO


class Stage:
    
    """
    A class used to represent the Stage entity and perform CRUD operations on it.
    Attributes
    ----------
    db_connection : DatabaseConnection
        An instance of DatabaseConnection to interact with the database.
    Methods
    -------
    create(data: StageDAO) -> int
        Inserts a new Stage record into the database.
    update(id_PK: int, data: StageDAO)
        Updates an existing Stage record in the database.
    delete(id_PK: int)
        Deletes a Stage record from the database by its primary key.
    get_by_id(id_PK: int) -> StageDAO
        Retrieves a Stage record from the database by its primary key.
    get_all() -> List[StageDAO]
        Retrieves all Stage records from the database.
    get_by_level(level: str) -> List[StageDAO]
        Retrieves Stage records from the database that match a specific level.
    """

    def __init__(self, db_connection: MySQLDatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: StageDAO) -> int:
       
        query = """
            INSERT INTO Stage(section_FK, level)
            VALUES (%s, %s);
        """
        values = (data.section_FK, data.level)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: StageDAO):
      
        query = """
            UPDATE Stage
            SET section_FK = %s, level = %s
            WHERE id_PK = %s;
        """
        values = (data.section_FK, data.level, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM Stage
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        self.db_connection.delete(query, values)

    def get_by_id(self, id_PK: int) -> StageDAO:
       
        query = """
            SELECT id_PK, section_FK, level
            FROM Stage
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[StageDAO]:
       
        query = """
            SELECT id_PK, section_FK, level
            FROM Stage;
        """
        return self.db_connection.get_many(query)
    
    def get_by_level(self, level: str) -> List[StageDAO]:
                    
        query = """
            SELECT id_PK, section_FK, level
            FROM Stage
            WHERE level = %s;
        """
        values = (level,)
        return self.db_connection.get_many(query, values)
