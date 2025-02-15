from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections import DatabaseConnection
from CRUD import ChallengesBoosters
from Dao import ChallengesBoostersDAO

"""
This module defines the FastAPI routes for managing ChallengesBoosters.
Routes:
    - GET /ChallengesBoosters/get_all: Retrieve all ChallengesBoosters.
    - GET /ChallengesBoosters/get_by_id/{id_ChallengesBoosters}: Retrieve a specific ChallengesBoosters by ID.
    - POST /ChallengesBoosters/create: Create a new ChallengesBoosters.
    - PUT /ChallengesBoosters/update/{id_ChallengesBoosters}: Update an existing ChallengesBoosters by ID.
    - DELETE /ChallengesBoosters/delete/{id_ChallengesBoosters}: Delete a specific ChallengesBoosters by ID.
Dependencies:
    - MySQLDatabaseConnection: Manages the connection to the MySQL database.
    - ChallengesBoosters: CRUD operations for ChallengesBoosters.
    - ChallengesBoostersDAO: Data Access Object for ChallengesBoosters.
Raises:
    - HTTPException: If the requested ChallengesBoosters is not found or if there is an error during creation, update, or deletion.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = DatabaseConnection()
challenges_boosters_crud = ChallengesBoosters(db_connection)


@router.get("/ChallengesBoosters/get_all", response_model=List[ChallengesBoostersDAO])
def get_all_ChallengesBoosters():
   
    challenges_boosters = challenges_boosters_crud.get_all()
    return challenges_boosters


@router.get("/ChallengesBoosters/get_by_id/{id_ChallengesBoosters}", response_model=ChallengesBoostersDAO)
def get_ChallengesBoosters_by_id(id_ChallengesBoosters: int):
 
    challenges_boosters = challenges_boosters_crud.get_by_id(id_ChallengesBoosters)
    if not challenges_boosters:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="ChallengesBoosters not found"
        )
    return challenges_boosters


@router.post("/ChallengesBoosters/create", response_model=int)
def create_ChallengesBoosters(data: ChallengesBoostersDAO):
    
    challenges_boosters_new = challenges_boosters_crud.create(data)
    return challenges_boosters_new


@router.put("/ChallengesBoosters/update/{id_ChallengesBoosters}")
def update_ChallengesBoosters(id_ChallengesBoosters: int, data: ChallengesBoostersDAO):
    
    try:
        challenges_boosters_crud.update(id_ChallengesBoosters, data)
        return {"detail": "ChallengesBoosters updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update ChallengesBoosters"
        ) from e


@router.delete("/ChallengesBoosters/delete/{id_ChallengesBoosters}")
def delete_ChallengesBoosters(id_ChallengesBoosters: int):
    
    try:
        challenges_boosters_crud.delete(id_ChallengesBoosters)
        return {"detail": "ChallengesBoosters deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete ChallengesBoosters"
        ) from e