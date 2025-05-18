from fastapi import FastAPI, Query
from models import Feedback

app = FastAPI()

@app.post("/feedback")
async def root(feedback: Feedback, is_premium: bool = Query(False)):
    try:
        if is_premium:
            return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён. Ваш отзыв будет рассмотрен в приоритетном порядке."}
        return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён"}
    except Exception as e:
        raise e
