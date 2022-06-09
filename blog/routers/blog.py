from fastapi import APIRouter, Depends, status, HTTPException
from blog import database, schemas, models
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all_blogs(db:Session=Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(request: schemas.Blog, db: Session=Depends(database.get_db)):
    blog_data = models.Blog(title=request.title, text=request.text, author=request.author, user_id=1)
    db.add(blog_data)
    db.commit()
    db.refresh(blog_data)
    return blog_data

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def blog(id, db:Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail":f"Blog with id {id} is not available"}
    return blog

@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'
    
@router.put("/update/{id}/", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db:Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} id not found")
    blog.update(title=request.title, text=request.text, author=request.author)
    db.commit()
    return 'Successfully'