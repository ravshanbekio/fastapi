from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post('/blog')
def create(request: schemas.Blog):
    return {'title':request.title, 'body':request.text, 'author':request.author}