from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    text: str
    author: str