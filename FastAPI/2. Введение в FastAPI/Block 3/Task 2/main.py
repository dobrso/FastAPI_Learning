from fastapi import FastAPI
from models import Feedback

app = FastAPI()

feedbacks = []

@app.post("/feedback")
async def root(feedback: Feedback):
    try:
        feedbacks.append(feedback)
        return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}
    except Exception as e:
        raise e
    