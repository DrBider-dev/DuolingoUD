from typing import List
from Connections import DatabaseConnection
from Dao import UserAchievementDAO


class UserAchievement:
    
    """
    A class used to represent User Achievements in the database.
    Attributes
    ----------
    db_connection : DatabaseConnection
        A connection object to interact with the database.
    Methods
    -------
    create(data: UserAchievementDAO) -> int
        Inserts a new user achievement record into the database.
    update(id_PK: int, data: UserAchievementDAO)
        Updates an existing user achievement record in the database.
    delete(id_PK: int)
        Deletes a user achievement record from the database.
    get_by_id(id_PK: int) -> UserAchievementDAO
        Retrieves a user achievement record by its primary key.
    get_all() -> List[UserAchievementDAO]
        Retrieves all user achievement records from the database.
    """

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: UserAchievementDAO) -> int:
       
        query = """
            INSERT INTO UserAchievement(User_FK, Achievement_FK)
            VALUES (%s, %s);
        """
        values = (data.User_FK, data.Achievement_FK)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: UserAchievementDAO):
      
        query = """
            UPDATE UserAchievement
            SET User_FK = %s, Achievement_FK = %s
            WHERE id_PK = %s;
        """
        values = (data.User_FK, data.Achievement_FK, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM UserAchievement
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> UserAchievementDAO:
       
        query = """
            SELECT id_PK, User_FK, Achievement_FK 
            FROM UserAchievement
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[UserAchievementDAO]:
       
        query = """
            SELECT id_PK, User_FK, Achievement_FK 
            FROM UserAchievement;
        """
        return self.db_connection.get_many(query)