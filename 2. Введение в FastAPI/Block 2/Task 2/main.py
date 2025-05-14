from fastapi import FastAPI
from models import User

app = FastAPI()

@app.post("/user")
async def root(user: User):
    isAdult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": isAdult
    }
