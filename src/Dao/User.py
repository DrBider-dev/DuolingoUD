from datetime import date
from Dao.Project_dao import ProjectDAO

class UserDAO(ProjectDAO):
    
    id_PK: int = -1
    name: str
    nickname: str
    joinDate: date
    division_FK: int
    timesInTop: int
    email: str
    password: str
    courses_FK: int
    achievements_FK: int
    followed: int
    followers: int
    gemsNumber: int
    livesNumber: int
    boostersNumber: int
    isPremium: bool