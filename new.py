from fastapi import FastAPI
from pydantic import BaseModel

class New(BaseModel):
    title: str
    text: str
    admin: str

app = FastAPI()

@app.get("/")
async def index():
    return {"message":"Hello World!!!"}

@app.get("/about")
async def about():
    return {"message":"This is about page"}

@app.get("/blog")
async def blog():
    return {"message":"This is blog page"}

@app.get("/blog/unpublished")
async def unpublished_blogs():
    return {"message":"This is unpublished blogs"}

@app.get("/blog/{blog_id}")
async def blog_id(blog_id: int):
    return {"message":blog_id}

@app.post("/blog")
async def new_blog(new: New):
    return {"data":f"Blog successfully created: \n{new}"}