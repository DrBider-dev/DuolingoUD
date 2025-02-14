from typing import List
from Connections import DatabaseConnection
from Dao import StageDAO


class Stage:

    def __init__(self, db_connection: DatabaseConnection):
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
