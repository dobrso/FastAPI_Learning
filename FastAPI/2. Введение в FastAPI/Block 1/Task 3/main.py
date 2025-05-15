from fastapi import FastAPI

app = FastAPI()


@app.post("/calculate")
async def calculate(firstNum: int, secondNum: int):
    result = firstNum + secondNum
    return {"result": result}
