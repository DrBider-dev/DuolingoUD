from typing import List

from fastapi import APIRouter, HTTPException, status

from Connections.PostgreSql_Connection import PostgresDatabaseConnection
from CRUD import Achievement
from Dao import AchievementDAO

"""
Achievement API Endpoints
This module provides API endpoints for managing Achievements using FastAPI.
It includes endpoints for retrieving, creating, updating, and deleting Achievements.
Endpoints:
    - GET /Achievements/get_all: Retrieve all Achievements.
    - GET /Achievements/get_by_id/{id_Achievement}: Retrieve an Achievement by its ID.
    - POST /Achievements/create: Create a new Achievement.
    - PUT /Achievement/update/{id_Achievement}: Update an existing Achievement by its ID.
    - DELETE /Achievements/delete/{id_Achievement}: Delete an Achievement by its ID.
Dependencies:
    - fastapi: FastAPI framework for building APIs.
    - typing: For type hinting.
    - Connections.MySql_Connection: Module for MySQL database connection.
    - CRUD: Module for CRUD operations on Achievements.
    - Dao: Data Access Object for Achievements.
Classes:
    - MySQLDatabaseConnection: Manages the MySQL database connection.
    - Achievement: Provides CRUD operations for Achievements.
    - AchievementDAO: Data Access Object for Achievements.
Functions:
    - get_all_Achievements: Retrieve all Achievements.
    - get_Achievement_by_id: Retrieve an Achievement by its ID.
    - create_Achievement: Create a new Achievement.
    - update_Achievement: Update an existing Achievement by its ID.
    - delete_Achievement: Delete an Achievement by its ID.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = PostgresDatabaseConnection()
Achievement_crud = Achievement(db_connection)


@router.get("/Achievements/get_all", response_model=List[AchievementDAO])
def get_all_Achievements():
   
    Achievements = Achievement_crud.get_all()
    return Achievements


@router.get("/Achievements/get_by_id/{id_Achievement}", response_model=AchievementDAO)
def get_Achievement_by_id(id_Achievement: int):
 
    Achievement = Achievement_crud.get_by_id(id_Achievement)
    if not Achievement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Stadium not found"
        )
    return Achievement


@router.post("/Achievements/create", response_model=int)
def create_Achievement(data: AchievementDAO):
    
    Achievement_new = Achievement_crud.create(data)
    return Achievement_new


@router.put("/Achievement/update/{id_Achievement}")
def update_Achievement(id_Achievement: int, data: AchievementDAO):
    
    try:
        Achievement_crud.update(id_Achievement, data)
        return {"detail": "Achievement updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Achuevement"
        ) from e


@router.delete("/Achievements/delete/{id_Achievement}")
def delete_Achievement(id_Achievement: int):
    
    try:
        Achievement_crud.delete(id_Achievement)
        return {"detail": "Achievement deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Achievement"
        ) from e
