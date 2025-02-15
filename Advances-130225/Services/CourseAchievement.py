from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import CourseAchievement
from Dao import CourseAchievementDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
course_achievement_crud = CourseAchievement(db_connection)


@router.get("/CourseAchievements/get_all", response_model=List[CourseAchievementDAO])
def get_all_CourseAchievements():
   
    course_achievements = course_achievement_crud.get_all()
    return course_achievements


@router.get("/CourseAchievements/get_by_id/{id_CourseAchievement}", response_model=CourseAchievementDAO)
def get_CourseAchievement_by_id(id_CourseAchievement: int):
 
    course_achievement = course_achievement_crud.get_by_id(id_CourseAchievement)
    if not course_achievement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="CourseAchievement not found"
        )
    return course_achievement


@router.post("/CourseAchievements/create", response_model=int)
def create_CourseAchievement(data: CourseAchievementDAO):
    
    course_achievement_new = course_achievement_crud.create(data)
    return course_achievement_new


@router.put("/CourseAchievements/update/{id_CourseAchievement}")
def update_CourseAchievement(id_CourseAchievement: int, data: CourseAchievementDAO):
    
    try:
        course_achievement_crud.update(id_CourseAchievement, data)
        return {"detail": "CourseAchievement updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update CourseAchievement"
        ) from e


@router.delete("/CourseAchievements/delete/{id_CourseAchievement}")
def delete_CourseAchievement(id_CourseAchievement: int):
    
    try:
        course_achievement_crud.delete(id_CourseAchievement)
        return {"detail": "CourseAchievement deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete CourseAchievement"
        ) from e