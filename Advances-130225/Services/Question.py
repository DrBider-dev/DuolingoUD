from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Question
from Dao import QuestionDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
question_crud = Question(db_connection)


@router.get("/Questions/get_all", response_model=List[QuestionDAO])
def get_all_Questions():
   
    questions = question_crud.get_all()
    return questions


@router.get("/Questions/get_by_id/{id_Question}", response_model=QuestionDAO)
def get_Question_by_id(id_Question: int):
 
    question = question_crud.get_by_id(id_Question)
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Question not found"
        )
    return question


@router.post("/Questions/create", response_model=int)
def create_Question(data: QuestionDAO):
    
    question_new = question_crud.create(data)
    return question_new


@router.put("/Questions/update/{id_Question}")
def update_Question(id_Question: int, data: QuestionDAO):
    
    try:
        question_crud.update(id_Question, data)
        return {"detail": "Question updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Question"
        ) from e


@router.delete("/Questions/delete/{id_Question}")
def delete_Question(id_Question: int):
    
    try:
        question_crud.delete(id_Question)
        return {"detail": "Question deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Question"
        ) from e

@router.get("/Questions/get_by_type/{type}", response_model=List[QuestionDAO])
def get_Question_by_type(type: str):
    questions = question_crud.get_by_type(type)
    if not questions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Question not found"
        )
    return questions