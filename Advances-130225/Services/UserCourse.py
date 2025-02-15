from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import UserCourse
from Dao import UserCourseDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
user_course_crud = UserCourse(db_connection)


@router.get("/UserCourses/get_all", response_model=List[UserCourseDAO])
def get_all_UserCourses():
   
    user_courses = user_course_crud.get_all()
    return user_courses


@router.get("/UserCourses/get_by_id/{id_UserCourse}", response_model=UserCourseDAO)
def get_UserCourse_by_id(id_UserCourse: int):
 
    user_course = user_course_crud.get_by_id(id_UserCourse)
    if not user_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="UserCourse not found"
        )
    return user_course


@router.post("/UserCourses/create", response_model=int)
def create_UserCourse(data: UserCourseDAO):
    
    user_course_new = user_course_crud.create(data)
    return user_course_new


@router.put("/UserCourses/update/{id_UserCourse}")
def update_UserCourse(id_UserCourse: int, data: UserCourseDAO):
    
    try:
        user_course_crud.update(id_UserCourse, data)
        return {"detail": "UserCourse updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update UserCourse"
        ) from e


@router.delete("/UserCourses/delete/{id_UserCourse}")
def delete_UserCourse(id_UserCourse: int):
    
    try:
        user_course_crud.delete(id_UserCourse)
        return {"detail": "UserCourse deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete UserCourse"
        ) from e