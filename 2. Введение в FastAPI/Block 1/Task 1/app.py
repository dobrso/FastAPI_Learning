from fastapi import FastAPI

app = FastAPI()

firstMessage = "Добро пожаловать в моё FastAPI приложение!"
secondMessage = "Авторелоад действительно работает"


@app.get("/")
async def root() -> None:
    return {"message": firstMessage}
