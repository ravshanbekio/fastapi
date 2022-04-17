from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .models import Blog

models.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session=Depends(get_db)):
    blog_data = models.Blog(title=request.title, text=request.text, author=request.author)
    db.add(blog_data)
    db.commit()
    db.refresh(blog_data)
    return blog_data

@app.get("/blog", status_code=status.HTTP_200_OK)
def all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def blog(id,response:Response, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail":f"Blog with id {id} is not available"}
    return blog

@app.delete("/blog/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'
