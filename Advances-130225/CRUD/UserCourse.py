from typing import List
from Connections import DatabaseConnection
from Dao import UserCourseDAO


class UserCourse:
    
    """
    A class to manage CRUD operations for the UserCourse table in the database.
    Attributes:
    -----------
    db_connection : DatabaseConnection
        An instance of the DatabaseConnection class to interact with the database.
    Methods:
    --------
    __init__(db_connection: DatabaseConnection):
        Initializes the UserCourse instance with a database connection and connects to the database.
    create(data: UserCourseDAO) -> int:
        Inserts a new record into the UserCourse table with the provided data and returns the ID of the created record.
    update(id_PK: int, data: UserCourseDAO):
        Updates an existing record in the UserCourse table identified by the given primary key with the provided data.
    delete(id_PK: int):
        Deletes a record from the UserCourse table identified by the given primary key.
    get_by_id(id_PK: int) -> UserCourseDAO:
        Retrieves a record from the UserCourse table identified by the given primary key and returns it as a UserCourseDAO object.
    get_all() -> List[UserCourseDAO]:
        Retrieves all records from the UserCourse table and returns them as a list of UserCourseDAO objects.
    """

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: UserCourseDAO) -> int:
       
        query = """
            INSERT INTO UserCourse(User_FK, Course_FK)
            VALUES (%s, %s);
        """
        values = (data.User_FK, data.Course_FK)
        return self.db_connection.create(query, values)

    def update(self, id_PK: int, data: UserCourseDAO):
      
        query = """
            UPDATE UserCourse
            SET User_FK = %s, Course_FK = %s
            WHERE id_PK = %s;
        """
        values = (data.User_FK, data.Course_FK, id_PK)
        self.db_connection.update(query, values)

    def delete(self, id_PK: int):
     
        query = """
            DELETE FROM UserCourse
            WHERE id_PK = %s;
        """
        self.db_connection.delete(query, id_PK)

    def get_by_id(self, id_PK: int) -> UserCourseDAO:
       
        query = """
            SELECT id_PK, User_FK, Course_FK 
            FROM UserCourse
            WHERE id_PK = %s;
        """
        values = (id_PK)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[UserCourseDAO]:
       
        query = """
            SELECT id_PK, User_FK, Course_FK 
            FROM UserCourse;
        """
        return self.db_connection.get_many(query)