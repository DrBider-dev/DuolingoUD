from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import LessonBoosters
from Dao import LessonBoostersDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
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