from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models, schemas

def get_blogs(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(request: schemas.Blog, db:Session):
    blog_data = models.Blog(title=request.title, text=request.text, author=request.author, user_id=1)
    db.add(blog_data)
    db.commit()
    db.refresh(blog_data)
    return blog_data

def destroy_blog(id: int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def put_blog(id: int, request: schemas.Blog ,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} id not found")
    blog.update(title=request.title, text=request.text, author=request.author)
    db.commit()
    return 'Successfully'

def get_blog(id:int ,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail":f"Blog with id {id} is not available"}
    return blog