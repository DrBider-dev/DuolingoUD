from typing import List
from Connections.MySql_Connection import MySQLDatabaseConnection
from Dao import DivisionDAO


class Division:
    
    """
    Division class to handle CRUD operations for the Division table in the database.
    Attributes:
        db_connection (DatabaseConnection): The database connection object.
    Methods:
        __init__(db_connection: DatabaseConnection):
            Initializes the Division class with a database connection and connects to the database.
        create(data: DivisionDAO) -> int:
            Inserts a new record into the Division table.
        update(id_PK: int, data: DivisionDAO):
            Updates an existing record in the Division table based on the primary key.
        delete(id_PK: int):
            Deletes a record from the Division table based on the primary key.
        get_by_id(id_PK: int) -> DivisionDAO:
            Retrieves a record from the Division table based on the primary key.
        get_all() -> List[DivisionDAO]:
            Retrieves all records from the Division table.
        get_by_name(name: str) -> List[DivisionDAO]:
            Retrieves records from the Division table where the name matches the given string.
    """

    def __init__(self, db_connection: MySQLDatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: DivisionDAO) -> int:
       
        query = """
            INSERT INTO Division(name, currentPosition, zone, users)
            VALUES (%s, %s, %s);
        """
        values = (data.name, data.currentPosition, data.zone, data.users)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: DivisionDAO):
      
        query = """
            UPDATE Division
            SET name = %s, currentPosition = %s, zone = %s, users = %s
            WHERE id_PK = %s;
        """
        values = (data.name, data.currentPosition, data.zone, data.users, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM Division
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> DivisionDAO:
       
        query = """
            SELECT id_PK, name, currentPosition, zone, users 
            FROM Division
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[DivisionDAO]:
       
        query = """
            SELECT id_PK, name, currentPosition, zone, users 
            FROM Division;
        """
        return self.db_connection.get_many(query)

    def get_by_name(self, name: str) -> List[DivisionDAO]:
   
        query = """
            SELECT id_PK, name, currentPosition, zone, users 
            FROM Division
            WHERE LOWER(name) LIKE LOWER(%s);
        """
        values = (f'%{name}%',)
        return self.db_connection.get_many(query, values)