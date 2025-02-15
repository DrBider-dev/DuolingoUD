from typing import List
from Connections import DatabaseConnection
from Dao import LessonBoostersDAO


class LessonBoosters:
    
    """
    A class to manage CRUD operations for LessonBoosters in the database.
    Attributes:
    db_connection (DatabaseConnection): The database connection object.
    Methods:
    __init__(db_connection: DatabaseConnection):
        Initializes the LessonBoosters object with a database connection.
    create(data: LessonBoostersDAO) -> int:
        Inserts a new record into the LessonBoosters table.
    update(id_PK: int, data: LessonBoostersDAO):
        Updates an existing record in the LessonBoosters table.
    delete(id_PK: int):
        Deletes a record from the LessonBoosters table by its primary key.
    get_by_id(id_PK: int) -> LessonBoostersDAO:
        Retrieves a record from the LessonBoosters table by its primary key.
    get_all() -> List[LessonBoostersDAO]:
        Retrieves all records from the LessonBoosters table.
    """

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: LessonBoostersDAO) -> int:
       
        query = """
            INSERT INTO LessonBoosters(Lesson_FK, Boosters_FK)
            VALUES (%s, %s);
        """
        values = (data.Lesson_FK, data.Boosters_FK)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: LessonBoostersDAO):
      
        query = """
            UPDATE LessonBoosters
            SET Lesson_FK = %s, Boosters_FK = %s
            WHERE id_PK = %s;
        """
        values = (data.Lesson_FK, data.Boosters_FK, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM LessonBoosters
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> LessonBoostersDAO:
       
        query = """
            SELECT id_PK, Lesson_FK, Boosters_FK 
            FROM LessonBoosters
            WHERE id_PK = %s;
        """
        values = (id_PK)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[LessonBoostersDAO]:
       
        query = """
            SELECT id_PK, Lesson_FK, Boosters_FK 
            FROM LessonBoosters;
        """
        return self.db_connection.get_many(query)