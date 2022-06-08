from fastapi import APIRouter, Depends, status, HTTPException
from blog import database, schemas, models
from typing import List
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/blog", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog], tags=["Blog"])
def all_blogs(db:Session=Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=["Blog"], response_model=schemas.ShowBlog)
def create(request: schemas.Blog, db: Session=Depends(database.get_db)):
    blog_data = models.Blog(title=request.title, text=request.text, author=request.author, user_id=1)
    db.add(blog_data)
    db.commit()
    db.refresh(blog_data)
    return blog_data

@router.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=["Blog"])
def blog(id, db:Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail":f"Blog with id {id} is not available"}
    return blog

@router.delete("/blog/delete/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blog"])
def destroy(id, db:Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'
    
@router.put("/blog/update/{id}/", status_code=status.HTTP_202_ACCEPTED, tags=["Blog"])
def update_blog(id, request: schemas.Blog, db:Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} id not found")
    blog.update(title=request.title, text=request.text, author=request.author)
    db.commit()
    return 'Successfully'