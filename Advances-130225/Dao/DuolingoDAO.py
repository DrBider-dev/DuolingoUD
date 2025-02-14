from datetime import time
from Dao.Project_dao import ProjectDAO

class QuestionDAO(ProjectDAO):
    
    id_PK: int = -1
    content: str
    answer: str
    isCorrect: bool
    question_type: str # Le cambie el nombre puesto que 'type' es una palabra reservada en Python

class DivisionDAO(ProjectDAO):

    id_PK: int = -1
    name: str
    currentPosition: int
    zone: str
    users: int

class ChallengesDAO(ProjectDAO):

    id_PK: int = -1
    description: str
    progress: int
    goal: int
    reward: str

class BoostersDAO(ProjectDAO):

    id_PK: int = -1
    name: str
    cost: int
    benefit: str
    maxNumber: int

class AchievementDAO(ProjectDAO):

    id_PK: int = -1
    name: str
    progressPercentage: float
    goal: str

class LessonDAO(ProjectDAO):

    id_PK: int = -1
    lesson_type: str # 'type' es palabra reservada
    questions_FK: int
    exp: int
    time: time
    accuracy: int

class SectionDAO(ProjectDAO):

    id_PK: int = -1
    name: str
    lessons_FK: int
    guide: str

class StageDAO(ProjectDAO):

    id_PK: int = -1
    section_FK: int
    level: str

class CourseDAO(ProjectDAO):

    id_PK: int = -1
    language: str
    stages_FK: int

class ProgressDAO(ProjectDAO):

    id_PK: int = -1
    course_FK: int
    user_FK: int
    streakDays: int
    dailyExp: int
    weeklyExp: int
    totalExp: int
    percentage: float

class UserCourseDAO(ProjectDAO):

    id_PK: int = -1
    User_FK: int
    Course_FK: int

class UserQuestionDAO(ProjectDAO):

    id_PK: int = -1
    User_FK: int
    Question_FK: int

class UserBoostersDAO(ProjectDAO):

    id_PK: int = -1
    User_FK: int
    Boosters_FK: int

class UserAchievementDAO(ProjectDAO):

    id_PK: int = -1
    User_FK: int
    Achievement_FK: int

class CourseAchievementDAO(ProjectDAO):

    id_PK: int = -1
    Course_FK: int
    Achievement_FK: int

class LessonBoostersDAO(ProjectDAO):

    id_PK: int = -1
    Lesson_FK: int
    Boosters_FK: int

class ChallengesBoostersDAO(ProjectDAO):

    id_PK: int = -1
    Challenges_FK: int
    Boosters_FK: int

class ChallengesAchievementDAO(ProjectDAO):

    id_PK: int = -1
    Challenges_FK: int
    Achievement_FK: int