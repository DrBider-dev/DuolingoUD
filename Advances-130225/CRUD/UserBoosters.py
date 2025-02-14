from typing import List
from Connections import DatabaseConnection
from Dao import UserBoostersDAO


class UserBoosters:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: UserBoostersDAO) -> int:
       
        query = """
            INSERT INTO UserBoosters(User_FK, Boosters_FK)
            VALUES (%s, %s);
        """
        values = (data.User_FK, data.Boosters_FK)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: UserBoostersDAO):
      
        query = """
            UPDATE UserBoosters
            SET User_FK = %s, Boosters_FK = %s
            WHERE id_PK = %s;
        """
        values = (data.User_FK, data.Boosters_FK, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM UserBoosters
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> UserBoostersDAO:
       
        query = """
            SELECT id_PK, User_FK, Boosters_FK 
            FROM UserBoosters
            WHERE id_PK = %s;
        """
        values = (id_PK)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[UserBoostersDAO]:
       
        query = """
            SELECT id_PK, User_FK, Boosters_FK 
            FROM UserBoosters;
        """
        return self.db_connection.get_many(query)