from typing import List
from Connections import DatabaseConnection
from Dao import DivisionDAO


class Division:

    def __init__(self, db_connection: DatabaseConnection):
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