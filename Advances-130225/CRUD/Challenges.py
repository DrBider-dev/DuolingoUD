from typing import List
from Connections import DatabaseConnection
from Dao import ChallengesDAO


class Challenges:

    def __init__(self, db_connection: DatabaseConnection):
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

    def get_by_name(self, name: str) -> List[ChallengesDAO]:
   
        query = """
            SELECT id_PK, description, progress, goal, reward 
            FROM Challenges;
            WHERE LOWER(name) LIKE LOWER(%s);
        """
        values = (f'%{name}%',)
        return self.db_connection.get_many(query, values)