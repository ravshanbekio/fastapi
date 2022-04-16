from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

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