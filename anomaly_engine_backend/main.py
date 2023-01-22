from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


"""
#!user payload notice
@app.get('/') will always return the full user payload
because we dont have a response model object 
being initiatived for the route. 
"""


@app.get("/")
def read_root():
    return []


