from fastapi import FastAPI

app = FastAPI()

@app.post("/feedback")
async def root(feedback):
    pass
