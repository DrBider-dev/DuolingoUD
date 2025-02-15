from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Course
from Dao import CourseDAO

"""
Course API Endpoints
This module defines the API endpoints for managing courses using FastAPI.
It includes endpoints for retrieving, creating, updating, and deleting courses.
Endpoints:
- GET /Courses/get_all: Retrieve all courses.
- GET /Courses/get_by_id/{id_Course}: Retrieve a course by its ID.
- POST /Courses/create: Create a new course.
- PUT /Courses/update/{id_Course}: Update an existing course by its ID.
- DELETE /Courses/delete/{id_Course}: Delete a course by its ID.
- GET /Courses/get_by_language/{language}: Retrieve courses by language.
Dependencies:
- MySQLDatabaseConnection: A class for managing MySQL database connections.
- Course: A CRUD class for managing course operations.
- CourseDAO: A data access object class for course data.
Raises:
- HTTPException: If a course is not found or if there is an error during creation, update, or deletion.
"""

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
course_crud = Course(db_connection)


@router.get("/Courses/get_all", response_model=List[CourseDAO])
def get_all_Courses():
   
    courses = course_crud.get_all()
    return courses


@router.get("/Courses/get_by_id/{id_Course}", response_model=CourseDAO)
def get_Course_by_id(id_Course: int):
 
    course = course_crud.get_by_id(id_Course)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Course not found"
        )
    return course


@router.post("/Courses/create", response_model=int)
def create_Course(data: CourseDAO):
    
    course_new = course_crud.create(data)
    return course_new


@router.put("/Courses/update/{id_Course}")
def update_Course(id_Course: int, data: CourseDAO):
    
    try:
        course_crud.update(id_Course, data)
        return {"detail": "Course updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Course"
        ) from e


@router.delete("/Courses/delete/{id_Course}")
def delete_Course(id_Course: int):
    
    try:
        course_crud.delete(id_Course)
        return {"detail": "Course deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Course"
        ) from e

@router.get("/Courses/get_by_language/{language}", response_model=List[CourseDAO])
def get_Course_by_language(language: str):
    courses = course_crud.get_by_language(language)
    if not courses:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Course not found"
        )
    return courses