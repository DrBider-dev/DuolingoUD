from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections import DatabaseConnection
from CRUD import UserBoosters
from Dao import UserBoostersDAO

"""
This module defines the FastAPI routes for managing UserBoosters.
Routes:
    - GET /UserBoosters/get_all: Retrieve all UserBoosters.
    - GET /UserBoosters/get_by_id/{id_UserBoosters}: Retrieve a UserBooster by its ID.
    - POST /UserBoosters/create: Create a new UserBooster.
    - PUT /UserBoosters/update/{id_UserBoosters}: Update an existing UserBooster by its ID.
    - DELETE /UserBoosters/delete/{id_UserBoosters}: Delete a UserBooster by its ID.
Dependencies:
    - MySQLDatabaseConnection: Manages the connection to the MySQL database.
    - UserBoosters: CRUD operations for UserBoosters.
    - UserBoostersDAO: Data Access Object for UserBoosters.
Exceptions:
    - HTTPException: Raised when a UserBooster is not found or when an operation fails.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = DatabaseConnection()
user_boosters_crud = UserBoosters(db_connection)


@router.get("/UserBoosters/get_all", response_model=List[UserBoostersDAO])
def get_all_UserBoosters():
   
    user_boosters = user_boosters_crud.get_all()
    return user_boosters


@router.get("/UserBoosters/get_by_id/{id_UserBoosters}", response_model=UserBoostersDAO)
def get_UserBoosters_by_id(id_UserBoosters: int):
 
    user_boosters = user_boosters_crud.get_by_id(id_UserBoosters)
    if not user_boosters:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="UserBoosters not found"
        )
    return user_boosters


@router.post("/UserBoosters/create", response_model=int)
def create_UserBoosters(data: UserBoostersDAO):
    
    user_boosters_new = user_boosters_crud.create(data)
    return user_boosters_new


@router.put("/UserBoosters/update/{id_UserBoosters}")
def update_UserBoosters(id_UserBoosters: int, data: UserBoostersDAO):
    
    try:
        user_boosters_crud.update(id_UserBoosters, data)
        return {"detail": "UserBoosters updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update UserBoosters"
        ) from e


@router.delete("/UserBoosters/delete/{id_UserBoosters}")
def delete_UserBoosters(id_UserBoosters: int):
    
    try:
        user_boosters_crud.delete(id_UserBoosters)
        return {"detail": "UserBoosters deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete UserBoosters"
        ) from e