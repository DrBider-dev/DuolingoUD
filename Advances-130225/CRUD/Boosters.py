from typing import List
from Connections import DatabaseConnection
from Dao import BoostersDAO


class Boosters:

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