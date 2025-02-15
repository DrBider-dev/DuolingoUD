from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections import DatabaseConnection
from CRUD import Boosters
from Dao import BoostersDAO

"""
This module defines the FastAPI routes for managing Boosters.
Routes:
    - GET /Boosters/get_all: Retrieve all Boosters.
    - GET /Boosters/get_by_id/{id_Booster}: Retrieve a Booster by its ID.
    - POST /Boosters/create: Create a new Booster.
    - PUT /Boosters/update/{id_Booster}: Update an existing Booster by its ID.
    - DELETE /Boosters/delete/{id_Booster}: Delete a Booster by its ID.
    - GET /Boosters/get_by_name/{name}: Retrieve a Booster by its name.
Dependencies:
    - MySQLDatabaseConnection: Manages the connection to the MySQL database.
    - Boosters: CRUD operations for Boosters.
    - BoostersDAO: Data Access Object for Boosters.
Exceptions:
    - HTTPException: Raised when a Booster is not found or an operation fails.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = DatabaseConnection()
boosters_crud = Boosters(db_connection)


@router.get("/Boosters/get_all", response_model=List[BoostersDAO])
def get_all_Boosters():
   
    boosters = boosters_crud.get_all()
    return boosters


@router.get("/Boosters/get_by_id/{id_Booster}", response_model=BoostersDAO)
def get_Booster_by_id(id_Booster: int):
 
    booster = boosters_crud.get_by_id(id_Booster)
    if not booster:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Booster not found"
        )
    return booster


@router.post("/Boosters/create", response_model=int)
def create_Booster(data: BoostersDAO):
    
    booster_new = boosters_crud.create(data)
    return booster_new


@router.put("/Boosters/update/{id_Booster}")
def update_Booster(id_Booster: int, data: BoostersDAO):
    
    try:
        boosters_crud.update(id_Booster, data)
        return {"detail": "Booster updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Booster"
        ) from e


@router.delete("/Boosters/delete/{id_Booster}")
def delete_Booster(id_Booster: int):
    
    try:
        boosters_crud.delete(id_Booster)
        return {"detail": "Booster deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Booster"
        ) from e

@router.get("/Boosters/get_by_name/{name}", response_model=BoostersDAO)
def get_Booster_by_name(name: str):
    booster = boosters_crud.get_by_name(name)
    if not booster:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Booster not found"
        )
    return booster