from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Stage
from Dao import StageDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
stage_crud = Stage(db_connection)


@router.get("/Stages/get_all", response_model=List[StageDAO])
def get_all_Stages():
   
    stages = stage_crud.get_all()
    return stages


@router.get("/Stages/get_by_id/{id_Stage}", response_model=StageDAO)
def get_Stage_by_id(id_Stage: int):
 
    stage = stage_crud.get_by_id(id_Stage)
    if not stage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Stage not found"
        )
    return stage


@router.post("/Stages/create", response_model=int)
def create_Stage(data: StageDAO):
    
    stage_new = stage_crud.create(data)
    return stage_new


@router.put("/Stages/update/{id_Stage}")
def update_Stage(id_Stage: int, data: StageDAO):
    
    try:
        stage_crud.update(id_Stage, data)
        return {"detail": "Stage updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Stage"
        ) from e


@router.delete("/Stages/delete/{id_Stage}")
def delete_Stage(id_Stage: int):
    
    try:
        stage_crud.delete(id_Stage)
        return {"detail": "Stage deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Stage"
        ) from e

@router.get("/Stages/get_by_level/{level}", response_model=List[StageDAO])
def get_Stage_by_level(level: str):
    stages = stage_crud.get_by_level(level)
    if not stages:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Stage not found"
        )
    return stages