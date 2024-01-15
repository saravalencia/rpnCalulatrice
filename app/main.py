from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from app import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
import csv
from io import StringIO

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Pydantic models
class CalculationInput(BaseModel):
    expression: str


class CalculationOutput(BaseModel):
    id: int
    expression: str
    result: str


# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@app.post("/calculate", response_model=CalculationOutput)
def calculate(input: CalculationInput, db: Session = Depends(get_db)):
    try:
        # Evaluate the expression
        result = evaluate(input.expression)

        # Store
        db_calculation = models.Calculation(expression=input.expression, result=result)
        db.add(db_calculation)
        db.commit()
        db.refresh(db_calculation)

        return db_calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/download-csv")
def download_csv(db: Session = Depends(get_db)):
    calculations = db.query(models.Calculation).all()

    stream = StringIO()
    csv_writer = csv.writer(stream)

    csv_writer.writerow(['ID', 'Expression', 'Result'])

    for calc in calculations:
        csv_writer.writerow([calc.id, calc.expression, calc.result])

    stream.seek(0)

    response = StreamingResponse(iter([stream.read()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=calculations.csv"

    return response
