from typing import List
from Connections import DatabaseConnection
from Dao import UserDAO


class User:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: UserDAO) -> int:
       
        query = """
            INSERT INTO User(name, nickname, joinDate, division_FK, timesInTop, email, password, courses_FK, achievements_FK, followed, followers, gemsNumber, livesNumber, boostersNumber, isPremium)
            VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (data.name, data.nickname, data.joinDate, data.division_FK, data.timesInTop, data.email, data.password, data.courses_FK, data.achievements_FK, data.followed, data.followers, data.gemsNumber, data.livesNumber, data.boostersNumber, data.isPremium)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: UserDAO):
      
        query = """
            UPDATE User
            SET name = %s, nickname = %s, joinDate = %s, division_FK = %s, timesInTop = %s, email = %s, password = %s, courses_FK = %s, achievements_FK = %s, followed = %s, followers = %s, gemsNumber = %s, livesNumber = %s, boostersNumber = %s, isPremium = %s
            WHERE id_PK = %s;
        """
        values = (data.name, data.progressPercentage, data.goal, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM User
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> UserDAO:
       
        query = """
            SELECT id_PK, name, nickname, joinDate, division_FK, timesInTop, email, courses_FK, achievements_FK, followed, followers, gemsNumber, livesNumber, boostersNumber, isPremium 
            FROM User
            WHERE id_PK = %s;
        """
        values = (id_PK)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[UserDAO]:
       
        query = """
            SELECT id_PK, name, nickname, email, isPremium 
            FROM User;
        """
        return self.db_connection.get_many(query)

    def get_by_name(self, name: str) -> List[UserDAO]:
   
        query = """
            SELECT id_PK, name, nickname, joinDate, division_FK, timesInTop, email, courses_FK, achievements_FK, followed, followers, gemsNumber, livesNumber, boostersNumber, isPremium 
            FROM User
            WHERE LOWER(name) LIKE LOWER(%s)
        """
        values = (f'%{name}%',)
        return self.db_connection.get_many(query, values)
    
    def get_by_email(self, email: str) -> List[UserDAO]:
            
          query = """
                SELECT id_PK, name, nickname, joinDate, division_FK, timesInTop, email, courses_FK, achievements_FK, followed, followers, gemsNumber, livesNumber, boostersNumber, isPremium 
                FROM User
                WHERE email = %s
          """
          values = (f'%{email}%',)
          return self.db_connection.get_many(query, values)
    
    def get_by_nickname(self, nickname: str) -> List[UserDAO]:
        
        query = """
            SELECT id_PK, name, nickname, joinDate, division_FK, timesInTop, email, courses_FK, achievements_FK, followed, followers, gemsNumber, livesNumber, boostersNumber, isPremium 
            FROM User
            WHERE nickname = %s
        """
        values = (f'%{nickname}%',)
        return self.db_connection.get_many(query, values)