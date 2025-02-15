from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Challenges
from Dao import ChallengesDAO

"""
This module defines the FastAPI routes for managing Challenges.
Routes:
    - GET /Challenges/get_all: Retrieve all challenges.
    - GET /Challenges/get_by_id/{id_Challenge}: Retrieve a challenge by its ID.
    - POST /Challenges/create: Create a new challenge.
    - PUT /Challenges/update/{id_Challenge}: Update an existing challenge by its ID.
    - DELETE /Challenges/delete/{id_Challenge}: Delete a challenge by its ID.
    - GET /Challenges/get_by_name/{name}: Retrieve a challenge by its name.
Dependencies:
    - MySQLDatabaseConnection: Manages the connection to the MySQL database.
    - Challenges: CRUD operations for challenges.
    - ChallengesDAO: Data Access Object for challenges.
Exceptions:
    - HTTPException: Raised when a challenge is not found or an operation fails.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
challenges_crud = Challenges(db_connection)


@router.get("/Challenges/get_all", response_model=List[ChallengesDAO])
def get_all_Challenges():
   
    challenges = challenges_crud.get_all()
    return challenges


@router.get("/Challenges/get_by_id/{id_Challenge}", response_model=ChallengesDAO)
def get_Challenge_by_id(id_Challenge: int):
 
    challenge = challenges_crud.get_by_id(id_Challenge)
    if not challenge:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Challenge not found"
        )
    return challenge


@router.post("/Challenges/create", response_model=int)
def create_Challenge(data: ChallengesDAO):
    
    challenge_new = challenges_crud.create(data)
    return challenge_new


@router.put("/Challenges/update/{id_Challenge}")
def update_Challenge(id_Challenge: int, data: ChallengesDAO):
    
    try:
        challenges_crud.update(id_Challenge, data)
        return {"detail": "Challenge updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Challenge"
        ) from e


@router.delete("/Challenges/delete/{id_Challenge}")
def delete_Challenge(id_Challenge: int):
    
    try:
        challenges_crud.delete(id_Challenge)
        return {"detail": "Challenge deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Challenge"
        ) from e

@router.get("/Challenges/get_by_name/{name}", response_model=ChallengesDAO)
def get_Challenge_by_name(name: str):
    challenge = challenges_crud.get_by_name(name)
    if not challenge:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Challenge not found"
        )
    return challenge