from typing import List
from Connections import DatabaseConnection
from Dao import SectionDAO


class Section:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: SectionDAO) -> int:
       
        query = """
            INSERT INTO Section(name, lessons_FK, guide)
            VALUES (%s, %s, %s);
        """
        values = (data.name, data.lessons_FK, data.guide)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: SectionDAO):
      
        query = """
            UPDATE Section
            SET name = %s, lessons_FK = %s, guide = %s
            WHERE id_PK = %s;
        """
        values = (data.name, data.lessons_FK, data.guide, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM Section
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        self.db_connection.delete(query, values)

    def get_by_id(self, id_PK: int) -> SectionDAO:
       
        query = """
            SELECT id_PK, name, lessons_FK, guide
            FROM Section
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[SectionDAO]:
       
        query = """
            SELECT id_PK, name, lessons_FK, guide
            FROM Section;
        """
        return self.db_connection.get_many(query)

    def get_by_name(self, name: str) -> List[SectionDAO]:
   
        query = """
            SELECT id_PK, name, lessons_FK, guide
            FROM Section
            WHERE name = %s;
        """
        values = (name,)
        return self.db_connection.get_many(query, values)