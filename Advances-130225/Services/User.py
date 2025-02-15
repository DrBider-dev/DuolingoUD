from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import User
from Dao import UserDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
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