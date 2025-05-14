from fastapi import FastAPI

app = FastAPI()


@app.post("/calculate")
async def calculate(firstNum: int, secondNum: int) -> None:
    result = firstNum + secondNum
    return {"result": result}
