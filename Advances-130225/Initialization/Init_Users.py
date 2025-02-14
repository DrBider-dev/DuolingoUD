"""
This script creates a few users in the database.
It uses the Faker library to generate fake data for the users.
The script connects to the database, creates a CRUD instance,
and then creates a few users using the CRUD instance.
The script prints the ID of the created users.

Author: Carlos Andres Sierra <cavirguezs@udistrital.edu.co>
"""

from faker import Faker

from Connections import DatabaseConnection
from Dao import UserDAO
from CRUD.User import User



class InitUsers:

    def __init__(self, conn: DatabaseConnection):

        self.conn = conn

    def create_users(self, n: int) -> bool:

        crud = User(self.conn)
        fake = Faker()

        try:
            for _ in range(n):
                # Generar datos con Faker según los campos de UserDAO
                id_PK = -1 
                name = fake.name()
                nickname = fake.user_name()
                joinDate = fake.date_this_month()  # datetime.date object
                division_FK = fake.random_int(min=1, max=5)  # Ejemplo: división entre 1-5
                timesInTop = fake.random_int(min=0, max=100)
                email = fake.email()
                password = fake.password()
                courses_FK = fake.random_int(min=1, max=10)  # Ejemplo: curso entre 1-10
                achievements_FK = fake.random_int(min=1, max=5)  # Ejemplo: logro entre 1-5
                followed = 0  # Valor inicial por defecto
                followers = 0
                gemsNumber = fake.random_int(min=0, max=1000)
                livesNumber = 5  # Valor inicial típico
                boostersNumber = 0
                isPremium = fake.boolean(chance_of_getting_true=25)  # 25% de ser premium

                data = UserDAO(
                    id_PK=id_PK,
                    name=name,
                    nickname=nickname,
                    joinDate=joinDate,
                    division_FK=division_FK,
                    timesInTop=timesInTop,
                    email=email,
                    password=password,
                    courses_FK=courses_FK,
                    achievements_FK=achievements_FK,
                    followed=followed,
                    followers=followers,
                    gemsNumber=gemsNumber,
                    livesNumber=livesNumber,
                    boostersNumber=boostersNumber,
                    isPremium=isPremium
                )
                user_id = crud.create(data)
                print(f"Created user with id: {user_id}")

            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False