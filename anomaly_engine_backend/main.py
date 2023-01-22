from fastapi import Depends, FastAPI, BackgroundTasks
from sqlalchemy.orm import Session

from . import crud, models, schemas
from os.path import exists
from .database import SessionLocal
import subprocess


app = FastAPI()


def create_db():
    test_db = exists('/testdb.db')

    if not test_db:
        subprocess.run(['touch', 'testdb.db'])
        

def run_migration():
    subprocess.run(['alembic', 'upgrade', 'head'])


@app.on_event('startup')
async def startup():
    create_db()
    run_migration()


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


app.post('/store-definition')


def data_definition_store(db: Session = Depends(get_db)):
    pass


@app.post('/store-ingest')
def data_ingest_initial(store_data: schemas.DataIngestPost, db: Session = Depends(get_db)):
    new_data = crud.store_ingest(db=db, DataIngest=store_data)
    return new_data
