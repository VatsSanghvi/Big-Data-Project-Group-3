from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import user
from schemas import user as schemas
from models import user as models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()


@app.post("/users/",response_model=schemas.User)
def post_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
    db_user = user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user.create_user(db=db,user=user)


@app.get("/users/", response_model=list[schemas.User])
def get_users(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    users = users.get_users(db,skip=skip,limit=limit)
    return users


@app.get("/users/{user_id}/",response_model=schemas.User)
def get_user(user_id:int, db:Session=Depends(get_db)):
    db_user = user.get_user(db,user_id =user_id )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/todos/",response_model=schemas.Todo)
def post_todo_for_user(user_id:int, todo:schemas.TodoCreate, db:Session=Depends(get_db)):
    return user.create_user_todo(db=db,user_id=user_id, todo=todo)
