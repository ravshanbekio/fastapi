from fastapi import APIRouter, status, HTTPException, Depends
from blog import schemas, models, database
from sqlalchemy.orm import Session
from blog.hashing import Hash

router = APIRouter()

@router.post("/create/user/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=["User"])
async def create_user(request: schemas.User, db:Session = Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email, username=request.username, country=request.country, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request

@router.get("/user/{id}/",response_model=schemas.ShowUser, tags=["User"])
async def get_user(id: int, db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is notfound!")
    return user