from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class CalculationInput(BaseModel):
    expression: str


def evaluate(expression: str) -> int:
    expression = expression.split()
    stack = []

    for ele in expression:
        if ele not in '/*+-':
            stack.append(int(ele))
        else:
            right = stack.pop()
            left = stack.pop()

            if ele == '+':
                stack.append(left + right)
            elif ele == '-':
                stack.append(left - right)
            elif ele == '*':
                stack.append(left * right)
            elif ele == '/':
                stack.append(int(left / right))

    return stack.pop()


@app.post("/calculate")
async def calculate(input: CalculationInput):
    try:
        result = evaluate(input.expression)
        return {result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
