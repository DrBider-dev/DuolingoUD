from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Achievement
from Dao import AchievementDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
stadiums_crud = AchievementDAO(db_connection)


@router.get("/Achievements/get_all", response_model=List[AchievementDAO])
def get_all_Achievements():
   
    Achievements = Achievement.get_all()
    return Achievements


@router.get("/Achievements/get_by_id/{id_Achievement}", response_model=AchievementDAO)
def get_Achievement_by_id(id_Achievement: int):
 
    Achievement = Achievement.get_by_id(id_Achievement)
    if not Achievement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Stadium not found"
        )
    return Achievement


@router.post("/Achievements/create", response_model=int)
def create_Achievement(data: AchievementDAO):
    
    Achievement_new = Achievement.create(data)
    return Achievement_new


@router.put("/Achievement/update/{id_Achievement}")
def update_stadium(id_Achievement: int, data: AchievementDAO):
    
    try:
        Achievement.update(Achievement, data)
        return {"detail": "Achievement updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update stadium"
        ) from e


@router.delete("/stadiums/delete/{id_stadium}")
def delete_stadium(id_stadium: int):
    
    try:
        stadiums_crud.delete(id_stadium)
        return {"detail": "Stadium deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete stadium"
        ) from e
