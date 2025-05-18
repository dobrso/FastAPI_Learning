from fastapi import FastAPI
from models import UserCreate

app = FastAPI()

@app.post("/create_user")
async def root(user: UserCreate):
    try:
        return user
    except Exception as e:
        raise e
    