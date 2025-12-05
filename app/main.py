from fastapi import FastAPI
from .database import Base, engine
from .routes import users

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User CRUD API")

app.include_router(users.router)

#run this main.py using uvicorn app.main:app --reload