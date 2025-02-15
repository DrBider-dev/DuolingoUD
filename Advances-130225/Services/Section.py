from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Section
from Dao import SectionDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
section_crud = Section(db_connection)


@router.get("/Sections/get_all", response_model=List[SectionDAO])
def get_all_Sections():
   
    sections = section_crud.get_all()
    return sections


@router.get("/Sections/get_by_id/{id_Section}", response_model=SectionDAO)
def get_Section_by_id(id_Section: int):
 
    section = section_crud.get_by_id(id_Section)
    if not section:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Section not found"
        )
    return section


@router.post("/Sections/create", response_model=int)
def create_Section(data: SectionDAO):
    
    section_new = section_crud.create(data)
    return section_new


@router.put("/Sections/update/{id_Section}")
def update_Section(id_Section: int, data: SectionDAO):
    
    try:
        section_crud.update(id_Section, data)
        return {"detail": "Section updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Section"
        ) from e


@router.delete("/Sections/delete/{id_Section}")
def delete_Section(id_Section: int):
    
    try:
        section_crud.delete(id_Section)
        return {"detail": "Section deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Section"
        ) from e

@router.get("/Sections/get_by_name/{name}", response_model=List[SectionDAO])
def get_Section_by_name(name: str):
    sections = section_crud.get_by_name(name)
    if not sections:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Section not found"
        )
    return sections