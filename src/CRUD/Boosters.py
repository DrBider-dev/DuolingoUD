from typing import List
from Connections import DatabaseConnection
from Dao import BoostersDAO


class Boosters:
    """
    A class to manage CRUD operations for Boosters in the database.
    Attributes:
    db_connection (DatabaseConnection): The database connection object.
    Methods:
    __init__(db_connection: DatabaseConnection):
        Initializes the Boosters class with a database connection and connects to the database.
    create(data: BoostersDAO) -> int:
        Inserts a new booster record into the database.
    update(id_PK: int, data: BoostersDAO):
        Updates an existing booster record in the database by its primary key.
    delete(id_PK: int):
        Deletes a booster record from the database by its primary key.
    get_by_id(id_PK: int) -> BoostersDAO:
        Retrieves a booster record from the database by its primary key.
    get_all() -> List[BoostersDAO]:
        Retrieves all booster records from the database.
    get_by_name(name: str) -> List[BoostersDAO]:
        Retrieves booster records from the database that match the given name.
    """
    
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: BoostersDAO) -> int:
       
        query = """
            INSERT INTO Boosters(name, cost, benefit, maxNumber)
            VALUES (%s, %s, %s, %s);
        """
        values = (data.name, data.cost, data.benefit, data.maxNumber)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: BoostersDAO):
         
          query = """
                UPDATE Boosters
                SET name = %s, cost = %s, benefit = %s, maxNumber = %s
                WHERE id_PK = %s;
          """
          values = (data.name, data.cost, data.benefit, data.maxNumber, id_PK)
          self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM Boosters
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> BoostersDAO:
       
        query = """
            SELECT id_PK, name, cost, benefit, maxNumber 
            FROM Boosters
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[BoostersDAO]:
       
        query = """
            SELECT id_PK, name, cost, benefit, maxNumber 
            FROM Boosters;
        """
        return self.db_connection.get_many(query)

    def get_by_name(self, name: str) -> List[BoostersDAO]:
   
        query = """
            SELECT id_PK, name, cost, benefit, maxNumber 
            FROM Boosters
            WHERE LOWER(name) LIKE LOWER(%s);
        """
        values = (f'%{name}%',)
        
        return self.db_connection.get_many(query, values)