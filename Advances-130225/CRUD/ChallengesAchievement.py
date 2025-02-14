from typing import List
from Connections import DatabaseConnection
from Dao import ChallengesAchievementDAO


class ChallengesAchievement:

    def __init__(self, db_connection: DatabaseConnection):
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
        values = (id_PK)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[ChallengesAchievementDAO]:
       
        query = """
            SELECT id_PK, Challenges_FK, Achievement_FK
            FROM ChallengesAchievement;
        """
        return self.db_connection.get_many(query)
