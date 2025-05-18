from fastapi import FastAPI
from models import Feedback

app = FastAPI()

@app.post("/feedback")
async def root(feedback: Feedback):
    return {"message": f"Feedback recieved. Thank you, {feedback.name}."}
