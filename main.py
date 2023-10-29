from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import uvicorn
import models
import schemas
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
import crud

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

origins = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"])

@app.get("/")
async def home(db:Session = Depends(get_db)) -> list[models.User]:
    return crud.get_all_users(db=db)

@app.post("/")
async def add_user(user:models.userCreate, db:Session = Depends(get_db)):
    return crud.add_user(db=db, user=user)



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)