from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

class Blog(BaseModel):
    title: str
    text: str
    published: Optional[bool] = None

app = FastAPI()

@app.get("/")
def home():
    return {'data':{'message':'Hello Everyone!!!'}}

@app.get('/about')
def about():
    return {'message':'This is an about page of this page'}

@app.get('/blog')
def blog(limit=3, published: bool = False, sort: Optional[str] = None):
    if published:
        return {"data":f"{limit} published blogs"}
    else:
        return {"data":f"{limit} unpublished blogs"}

@app.get('/blog/unread')
def unread_blog():
    return {"message":"This is unread messages page"}

@app.get('/blog/{blogid}')
def blog(blogid: int):
    return {"data":f"Lorem ipsum dolor amet...{blogid}"}

@app.get('/blog/{blog_id}/comments/')
def comments(blog_id, limit=10):
    return {"data":{"message":f"Blog id: {blog_id}'s comments"}}

@app.post('/blog')
def newblog(request: Blog):
    return {"blog_data":f"Blog title is - '{request.title}'"}

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1',port=9000)