from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    text: str
    author: str

    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    username: str
    country: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    username: str
    blogs:List[Blog]

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title : str
    text: str
    author: str
    owner: ShowUser

    class Config():
        orm_mode = True