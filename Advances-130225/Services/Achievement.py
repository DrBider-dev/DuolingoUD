from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Achievement
from Dao import AchievementDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
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
