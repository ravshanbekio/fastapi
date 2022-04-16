from fastapi import FastAPI, Depends
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

@app.post('/blog')
def create(request: schemas.Blog, db: Session=Depends(get_db)):
    blog_data = models.Blog(title=request.title, text=request.text, author=request.author)
    db.add(blog_data)
    db.commit()
    db.refresh(blog_data)
    return blog_data

@app.get("/blog")
def all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

@app.get("/blog/{id}")
def blog(id, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog