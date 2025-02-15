from Connections.MySql_Connection import MySQLDatabaseConnection
from Dao import ProgressDAO


class Progress:

    """
    The Progress class provides CRUD operations for the Progress table in the database.
    Attributes:
        db_connection (DatabaseConnection): The database connection object.
    Methods:
        __init__(db_connection: DatabaseConnection):
            Initializes the Progress class with a database connection and connects to the database.
        create(data: ProgressDAO) -> int:
            Inserts a new record into the Progress table.
            Args:
                data (ProgressDAO): The data to be inserted.
            Returns:
                int: The ID of the newly created record.
        update(id_PK: int, data: ProgressDAO):
            Updates an existing record in the Progress table.
            Args:
                id_PK (int): The primary key of the record to be updated.
                data (ProgressDAO): The new data for the record.
        delete(id_PK: int):
            Deletes a record from the Progress table.
            Args:
                id_PK (int): The primary key of the record to be deleted.
        get_by_id(id_PK: int) -> ProgressDAO:
            Retrieves a record from the Progress table by its primary key.
            Args:
                id_PK (int): The primary key of the record to be retrieved.
            Returns:
                ProgressDAO: The data of the retrieved record.
    """

    def __init__(self, db_connection: MySQLDatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: ProgressDAO) -> int:
       
        query = """
            INSERT INTO Progress(course_FK, user_FK, streakDays, dailyExp, weeklyExp, totalExp, percentage)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        values = (data.course_FK, data.user_FK, data.streakDays, data.dailyExp, data.weeklyExp, data.totalExp, data.percentage)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: ProgressDAO):
      
        query = """
            UPDATE Progress
            SET course_FK = %s, user_FK = %s, streakDays = %s, dailyExp = %s, weeklyExp = %s, totalExp = %s, percentage = %s
            WHERE id_PK = %s;
        """
        values = (data.course_FK, data.user_FK, data.streakDays, data.dailyExp, data.weeklyExp, data.totalExp, data.percentage, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM Progress
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        self.db_connection.delete(query, values)

    def get_by_id(self, id_PK: int) -> ProgressDAO:
       
        query = """
            SELECT id_PK, course_FK, user_FK, streakDays, dailyExp, weeklyExp, totalExp, percentage
            FROM Progress
            WHERE id_PK = %s;
        """
        values = (id_PK,)
        return self.db_connection.get_one(query, values)