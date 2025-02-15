from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Progress
from Dao import ProgressDAO

"""
This module defines the FastAPI routes for managing Progress entities.
Routes:
    - GET /Progress/get_by_id/{id_Progress}: Retrieve a Progress entity by its ID.
    - POST /Progress/create: Create a new Progress entity.
    - PUT /Progress/update/{id_Progress}: Update an existing Progress entity by its ID.
    - DELETE /Progress/delete/{id_Progress}: Delete a Progress entity by its ID.
Dependencies:
    - MySQLDatabaseConnection: Manages the connection to the MySQL database.
    - Progress: CRUD operations for Progress entities.
    - ProgressDAO: Data Access Object for Progress entities.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
progress_crud = Progress(db_connection)

@router.get("/Progress/get_by_id/{id_Progress}", response_model=ProgressDAO)
def get_Progress_by_id(id_Progress: int):
 
    progress = progress_crud.get_by_id(id_Progress)
    if not progress:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Progress not found"
        )
    return progress


@router.post("/Progress/create", response_model=int)
def create_Progress(data: ProgressDAO):
    
    progress_new = progress_crud.create(data)
    return progress_new


@router.put("/Progress/update/{id_Progress}")
def update_Progress(id_Progress: int, data: ProgressDAO):
    
    try:
        progress_crud.update(id_Progress, data)
        return {"detail": "Progress updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Progress"
        ) from e


@router.delete("/Progress/delete/{id_Progress}")
def delete_Progress(id_Progress: int):
    
    try:
        progress_crud.delete(id_Progress)
        return {"detail": "Progress deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Progress"
        ) from e