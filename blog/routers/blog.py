from fastapi import APIRouter, Depends, status, HTTPException
from blog import database, schemas, models
from typing import List
from sqlalchemy.orm import Session
from blog.repository.query import *

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all_blogs(db:Session=Depends(database.get_db)):
    return get_blogs(db)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(request: schemas.Blog, db: Session=Depends(database.get_db)):
    return create_blog(request, db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def blog(id, db:Session=Depends(database.get_db)):
    return get_blog(id, db)

@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(database.get_db)):
    return destroy_blog(id, db)
    
@router.put("/update/{id}/", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db:Session=Depends(database.get_db)):
    return put_blog(id, request, db)