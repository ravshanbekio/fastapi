from fastapi import FastAPI
from typing import Optional

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