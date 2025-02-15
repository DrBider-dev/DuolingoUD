from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections import DatabaseConnection
from CRUD import ChallengesAchievement
from Dao import ChallengesAchievementDAO

"""
This module defines the FastAPI routes for managing ChallengesAchievement entities.
Routes:
    - GET /ChallengesAchievement/get_all: Retrieve all ChallengesAchievement records.
    - GET /ChallengesAchievement/get_by_id/{id_ChallengesAchievement}: Retrieve a specific ChallengesAchievement by its ID.
    - POST /ChallengesAchievement/create: Create a new ChallengesAchievement record.
    - PUT /ChallengesAchievement/update/{id_ChallengesAchievement}: Update an existing ChallengesAchievement record by its ID.
    - DELETE /ChallengesAchievement/delete/{id_ChallengesAchievement}: Delete a specific ChallengesAchievement by its ID.
Dependencies:
    - fastapi.APIRouter: For creating route handlers.
    - fastapi.HTTPException: For raising HTTP exceptions.
    - fastapi.status: For HTTP status codes.
    - typing.List: For type hinting.
    - Connections.MySql_Connection.MySQLDatabaseConnection: For database connection.
    - CRUD.ChallengesAchievement: For CRUD operations on ChallengesAchievement.
    - Dao.ChallengesAchievementDAO: Data Access Object for ChallengesAchievement.
Attributes:
    router (APIRouter): The FastAPI router instance for defining routes.
    db_connection (MySQLDatabaseConnection): The database connection instance.
    challenges_achievement_crud (ChallengesAchievement): The CRUD instance for ChallengesAchievement operations.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = DatabaseConnection()
challenges_achievement_crud = ChallengesAchievement(db_connection)


@router.get("/ChallengesAchievement/get_all", response_model=List[ChallengesAchievementDAO])
def get_all_ChallengesAchievements():
   
    challenges_achievements = challenges_achievement_crud.get_all()
    return challenges_achievements


@router.get("/ChallengesAchievement/get_by_id/{id_ChallengesAchievement}", response_model=ChallengesAchievementDAO)
def get_ChallengesAchievement_by_id(id_ChallengesAchievement: int):
 
    challenges_achievement = challenges_achievement_crud.get_by_id(id_ChallengesAchievement)
    if not challenges_achievement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="ChallengesAchievement not found"
        )
    return challenges_achievement


@router.post("/ChallengesAchievement/create", response_model=int)
def create_ChallengesAchievement(data: ChallengesAchievementDAO):
    
    challenges_achievement_new = challenges_achievement_crud.create(data)
    return challenges_achievement_new


@router.put("/ChallengesAchievement/update/{id_ChallengesAchievement}")
def update_ChallengesAchievement(id_ChallengesAchievement: int, data: ChallengesAchievementDAO):
    
    try:
        challenges_achievement_crud.update(id_ChallengesAchievement, data)
        return {"detail": "ChallengesAchievement updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update ChallengesAchievement"
        ) from e


@router.delete("/ChallengesAchievement/delete/{id_ChallengesAchievement}")
def delete_ChallengesAchievement(id_ChallengesAchievement: int):
    
    try:
        challenges_achievement_crud.delete(id_ChallengesAchievement)
        return {"detail": "ChallengesAchievement deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete ChallengesAchievement"
        ) from e