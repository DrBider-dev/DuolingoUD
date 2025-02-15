from typing import List
from fastapi import APIRouter, HTTPException, status

from Connections.MySql_Connection import MySQLDatabaseConnection
from CRUD import Boosters
from Dao import BoostersDAO

router = APIRouter()

# Initialize MySQL DB connection and CRUD class.
db_connection = MySQLDatabaseConnection()
boosters_crud = Boosters(db_connection)


@router.get("/Boosters/get_all", response_model=List[BoostersDAO])
def get_all_Boosters():
   
    boosters = boosters_crud.get_all()
    return boosters


@router.get("/Boosters/get_by_id/{id_Booster}", response_model=BoostersDAO)
def get_Booster_by_id(id_Booster: int):
 
    booster = boosters_crud.get_by_id(id_Booster)
    if not booster:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Booster not found"
        )
    return booster


@router.post("/Boosters/create", response_model=int)
def create_Booster(data: BoostersDAO):
    
    booster_new = boosters_crud.create(data)
    return booster_new


@router.put("/Boosters/update/{id_Booster}")
def update_Booster(id_Booster: int, data: BoostersDAO):
    
    try:
        boosters_crud.update(id_Booster, data)
        return {"detail": "Booster updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not update Booster"
        ) from e


@router.delete("/Boosters/delete/{id_Booster}")
def delete_Booster(id_Booster: int):
    
    try:
        boosters_crud.delete(id_Booster)
        return {"detail": "Booster deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not delete Booster"
        ) from e

@router.get("/Boosters/get_by_name/{name}", response_model=BoostersDAO)
def get_Booster_by_name(name: str):
    booster = boosters_crud.get_by_name(name)
    if not booster:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Booster not found"
        )
    return booster