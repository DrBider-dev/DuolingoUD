from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections import DatabaseConnection
from CRUD import User
from Dao import UserDAO

"""
This module defines the User-related API endpoints using FastAPI.
Endpoints:
- GET /Users/get_all: Retrieve all users.
- GET /Users/get_by_id/{id_User}: Retrieve a user by their ID.
- POST /Users/create: Create a new user.
- PUT /Users/update/{id_User}: Update an existing user by their ID.
- DELETE /Users/delete/{id_User}: Delete a user by their ID.
- GET /Users/get_by_name/{name}: Retrieve users by their name.
- GET /Users/get_by_email/{email}: Retrieve users by their email.
- GET /Users/get_by_nickname/{nickname}: Retrieve users by their nickname.
Dependencies:
- MySQLDatabaseConnection: Manages the connection to the MySQL database.
- User: CRUD operations for the User entity.
- UserDAO: Data Access Object for the User entity.
Raises:
- HTTPException: If a user is not found or if there is an error during creation, update, or deletion.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = DatabaseConnection()
user_crud = User(db_connection)


@router.get("/Users/get_all", response_model=List[UserDAO])
def get_all_Users():
   
    users = user_crud.get_all()
    return users


@router.get("/Users/get_by_id/{id_User}", response_model=UserDAO)
def get_User_by_id(id_User: int):
 
    user = user_crud.get_by_id(id_User)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@router.post("/Users/create", response_model=int)
def create_User(data: UserDAO):
    
    user_new = user_crud.create(data)
    return user_new


@router.put("/Users/update/{id_User}")
def update_User(id_User: int, data: UserDAO):
    
    try:
        user_crud.update(id_User, data)
        return {"detail": "User updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update User"
        ) from e


@router.delete("/Users/delete/{id_User}")
def delete_User(id_User: int):
    
    try:
        user_crud.delete(id_User)
        return {"detail": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete User"
        ) from e

@router.get("/Users/get_by_name/{name}", response_model=List[UserDAO])
def get_User_by_name(name: str):
    users = user_crud.get_by_name(name)
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return users

@router.get("/Users/get_by_email/{email}", response_model=List[UserDAO])
def get_User_by_email(email: str):
    users = user_crud.get_by_email(email)
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return users

@router.get("/Users/get_by_nickname/{nickname}", response_model=List[UserDAO])
def get_User_by_nickname(nickname: str):
    users = user_crud.get_by_nickname(nickname)
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return users