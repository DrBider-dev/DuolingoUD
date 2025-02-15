from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import UserAchievement
from Dao import UserAchievementDAO

"""
This module defines the FastAPI routes for managing UserAchievements.
Routes:
    - GET /UserAchievements/get_all: Retrieve all UserAchievements.
    - GET /UserAchievements/get_by_id/{id_UserAchievement}: Retrieve a UserAchievement by its ID.
    - POST /UserAchievements/create: Create a new UserAchievement.
    - PUT /UserAchievements/update/{id_UserAchievement}: Update an existing UserAchievement by its ID.
    - DELETE /UserAchievements/delete/{id_UserAchievement}: Delete a UserAchievement by its ID.
Dependencies:
    - fastapi.APIRouter: For creating route handlers.
    - fastapi.HTTPException: For raising HTTP exceptions.
    - fastapi.status: For HTTP status codes.
    - typing.List: For type hinting lists.
    - Connections.MySql_Connection.MySQLDatabaseConnection: For MySQL database connection.
    - CRUD.UserAchievement: For CRUD operations on UserAchievements.
    - Dao.UserAchievementDAO: For data access object representing UserAchievement.
Initialization:
    - Initializes MySQL database connection.
    - Initializes UserAchievement CRUD operations with the database connection.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
user_achievement_crud = UserAchievement(db_connection)


@router.get("/UserAchievements/get_all", response_model=List[UserAchievementDAO])
def get_all_UserAchievements():
   
    user_achievements = user_achievement_crud.get_all()
    return user_achievements


@router.get("/UserAchievements/get_by_id/{id_UserAchievement}", response_model=UserAchievementDAO)
def get_UserAchievement_by_id(id_UserAchievement: int):
 
    user_achievement = user_achievement_crud.get_by_id(id_UserAchievement)
    if not user_achievement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="UserAchievement not found"
        )
    return user_achievement


@router.post("/UserAchievements/create", response_model=int)
def create_UserAchievement(data: UserAchievementDAO):
    
    user_achievement_new = user_achievement_crud.create(data)
    return user_achievement_new


@router.put("/UserAchievements/update/{id_UserAchievement}")
def update_UserAchievement(id_UserAchievement: int, data: UserAchievementDAO):
    
    try:
        user_achievement_crud.update(id_UserAchievement, data)
        return {"detail": "UserAchievement updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update UserAchievement"
        ) from e


@router.delete("/UserAchievements/delete/{id_UserAchievement}")
def delete_UserAchievement(id_UserAchievement: int):
    
    try:
        user_achievement_crud.delete(id_UserAchievement)
        return {"detail": "UserAchievement deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete UserAchievement"
        ) from e