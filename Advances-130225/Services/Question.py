from typing import List
from fastapi import APIRouter, HTTPException, status
from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Question
from Dao import QuestionDAO

"""
This module defines the FastAPI routes for managing Questions.
Routes:
    - GET /Questions/get_all: Retrieve all questions.
    - GET /Questions/get_by_id/{id_Question}: Retrieve a question by its ID.
    - POST /Questions/create: Create a new question.
    - PUT /Questions/update/{id_Question}: Update an existing question by its ID.
    - DELETE /Questions/delete/{id_Question}: Delete a question by its ID.
    - GET /Questions/get_by_type/{type}: Retrieve questions by their type.
Dependencies:
    - MySQLDatabaseConnection: Manages the connection to the MySQL database.
    - Question: CRUD operations for questions.
    - QuestionDAO: Data Access Object for questions.
"""

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