from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Lesson
from Dao import LessonDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
lesson_crud = Lesson(db_connection)


@router.get("/Lessons/get_all", response_model=List[LessonDAO])
def get_all_Lessons():
   
    lessons = lesson_crud.get_all()
    return lessons


@router.get("/Lessons/get_by_id/{id_Lesson}", response_model=LessonDAO)
def get_Lesson_by_id(id_Lesson: int):
 
    lesson = lesson_crud.get_by_id(id_Lesson)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found"
        )
    return lesson


@router.post("/Lessons/create", response_model=int)
def create_Lesson(data: LessonDAO):
    
    lesson_new = lesson_crud.create(data)
    return lesson_new


@router.put("/Lessons/update/{id_Lesson}")
def update_Lesson(id_Lesson: int, data: LessonDAO):
    
    try:
        lesson_crud.update(id_Lesson, data)
        return {"detail": "Lesson updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Lesson"
        ) from e


@router.delete("/Lessons/delete/{id_Lesson}")
def delete_Lesson(id_Lesson: int):
    
    try:
        lesson_crud.delete(id_Lesson)
        return {"detail": "Lesson deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Lesson"
        ) from e