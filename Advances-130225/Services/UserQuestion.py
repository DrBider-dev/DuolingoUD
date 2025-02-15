from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import UserQuestion
from Dao import UserQuestionDAO

"""
This module provides API endpoints for managing UserQuestions.
Endpoints:
- GET /UserQuestions/get_all: Retrieve all UserQuestions.
- GET /UserQuestions/get_by_id/{id_UserQuestion}: Retrieve a UserQuestion by its ID.
- POST /UserQuestions/create: Create a new UserQuestion.
- PUT /UserQuestions/update/{id_UserQuestion}: Update an existing UserQuestion by its ID.
- DELETE /UserQuestions/delete/{id_UserQuestion}: Delete a UserQuestion by its ID.
Dependencies:
- MySQLDatabaseConnection: Manages the connection to the MySQL database.
- UserQuestion: CRUD operations for UserQuestions.
- UserQuestionDAO: Data Access Object for UserQuestions.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
user_question_crud = UserQuestion(db_connection)


@router.get("/UserQuestions/get_all", response_model=List[UserQuestionDAO])
def get_all_UserQuestions():
   
    user_questions = user_question_crud.get_all()
    return user_questions


@router.get("/UserQuestions/get_by_id/{id_UserQuestion}", response_model=UserQuestionDAO)
def get_UserQuestion_by_id(id_UserQuestion: int):
 
    user_question = user_question_crud.get_by_id(id_UserQuestion)
    if not user_question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="UserQuestion not found"
        )
    return user_question


@router.post("/UserQuestions/create", response_model=int)
def create_UserQuestion(data: UserQuestionDAO):
    
    user_question_new = user_question_crud.create(data)
    return user_question_new


@router.put("/UserQuestions/update/{id_UserQuestion}")
def update_UserQuestion(id_UserQuestion: int, data: UserQuestionDAO):
    
    try:
        user_question_crud.update(id_UserQuestion, data)
        return {"detail": "UserQuestion updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update UserQuestion"
        ) from e


@router.delete("/UserQuestions/delete/{id_UserQuestion}")
def delete_UserQuestion(id_UserQuestion: int):
    
    try:
        user_question_crud.delete(id_UserQuestion)
        return {"detail": "UserQuestion deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete UserQuestion"
        ) from e