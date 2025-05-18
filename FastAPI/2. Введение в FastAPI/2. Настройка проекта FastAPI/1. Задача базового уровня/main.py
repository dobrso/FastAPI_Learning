from fastapi import FastAPI
from models import User

app = FastAPI()

user = User(name="John Doe", id=1)

@app.get("/users")
async def root():
    return user
