from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    text: str
    author: str

class ShowBlog(BaseModel):
    title : str
    text: str
    author: str
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    username: str
    country: str