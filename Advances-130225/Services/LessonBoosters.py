from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections import DatabaseConnection
from CRUD import LessonBoosters
from Dao import LessonBoostersDAO

"""
This module defines the FastAPI routes for managing LessonBoosters.
Routes:
    - GET /LessonBoosters/get_all: Retrieve all LessonBoosters.
    - GET /LessonBoosters/get_by_id/{id_LessonBoosters}: Retrieve a specific LessonBooster by its ID.
    - POST /LessonBoosters/create: Create a new LessonBooster.
    - PUT /LessonBoosters/update/{id_LessonBoosters}: Update an existing LessonBooster by its ID.
    - DELETE /LessonBoosters/delete/{id_LessonBoosters}: Delete a specific LessonBooster by its ID.
Dependencies:
    - fastapi.APIRouter: For creating route handlers.
    - fastapi.HTTPException: For raising HTTP exceptions.
    - fastapi.status: For HTTP status codes.
    - typing.List: For type hinting.
    - Connections.MySql_Connection.MySQLDatabaseConnection: For database connection.
    - CRUD.LessonBoosters: For CRUD operations on LessonBoosters.
    - Dao.LessonBoostersDAO: For data access object of LessonBoosters.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = DatabaseConnection()
lesson_boosters_crud = LessonBoosters(db_connection)


@router.get("/LessonBoosters/get_all", response_model=List[LessonBoostersDAO])
def get_all_LessonBoosters():
   
    lesson_boosters = lesson_boosters_crud.get_all()
    return lesson_boosters


@router.get("/LessonBoosters/get_by_id/{id_LessonBoosters}", response_model=LessonBoostersDAO)
def get_LessonBoosters_by_id(id_LessonBoosters: int):
 
    lesson_boosters = lesson_boosters_crud.get_by_id(id_LessonBoosters)
    if not lesson_boosters:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="LessonBoosters not found"
        )
    return lesson_boosters


@router.post("/LessonBoosters/create", response_model=int)
def create_LessonBoosters(data: LessonBoostersDAO):
    
    lesson_boosters_new = lesson_boosters_crud.create(data)
    return lesson_boosters_new


@router.put("/LessonBoosters/update/{id_LessonBoosters}")
def update_LessonBoosters(id_LessonBoosters: int, data: LessonBoostersDAO):
    
    try:
        lesson_boosters_crud.update(id_LessonBoosters, data)
        return {"detail": "LessonBoosters updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update LessonBoosters"
        ) from e


@router.delete("/LessonBoosters/delete/{id_LessonBoosters}")
def delete_LessonBoosters(id_LessonBoosters: int):
    
    try:
        lesson_boosters_crud.delete(id_LessonBoosters)
        return {"detail": "LessonBoosters deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete LessonBoosters"
        ) from e