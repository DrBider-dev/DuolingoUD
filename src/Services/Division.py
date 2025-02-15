from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Division
from Dao import DivisionDAO

"""
This module provides API endpoints for managing Divisions using FastAPI.
Endpoints:
- GET /Divisions/get_all: Retrieve all divisions.
- GET /Divisions/get_by_id/{id_Division}: Retrieve a division by its ID.
- POST /Divisions/create: Create a new division.
- PUT /Divisions/update/{id_Division}: Update an existing division by its ID.
- DELETE /Divisions/delete/{id_Division}: Delete a division by its ID.
- GET /Divisions/get_by_name/{name}: Retrieve divisions by their name.
Dependencies:
- MySQLDatabaseConnection: Handles the connection to the MySQL database.
- Division: CRUD operations for the Division entity.
- DivisionDAO: Data Access Object for the Division entity.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
division_crud = Division(db_connection)


@router.get("/Divisions/get_all", response_model=List[DivisionDAO])
def get_all_Divisions():
   
    divisions = division_crud.get_all()
    return divisions


@router.get("/Divisions/get_by_id/{id_Division}", response_model=DivisionDAO)
def get_Division_by_id(id_Division: int):
 
    division = division_crud.get_by_id(id_Division)
    if not division:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Division not found"
        )
    return division


@router.post("/Divisions/create", response_model=int)
def create_Division(data: DivisionDAO):
    
    division_new = division_crud.create(data)
    return division_new


@router.put("/Divisions/update/{id_Division}")
def update_Division(id_Division: int, data: DivisionDAO):
    
    try:
        division_crud.update(id_Division, data)
        return {"detail": "Division updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Division"
        ) from e


@router.delete("/Divisions/delete/{id_Division}")
def delete_Division(id_Division: int):
    
    try:
        division_crud.delete(id_Division)
        return {"detail": "Division deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Division"
        ) from e

@router.get("/Divisions/get_by_name/{name}", response_model=List[DivisionDAO])
def get_Division_by_name(name: str):
    divisions = division_crud.get_by_name(name)
    if not divisions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Division not found"
        )
    return divisions