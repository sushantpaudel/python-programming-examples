"""Lab 1 - Question 25: Simple calculator API using FastAPI."""

from fastapi import FastAPI, HTTPException, Query
import uvicorn

app = FastAPI(title="Lab 1 - Question 25", version="1.0")

OPERATIONS = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b,
}


@app.get("/calculate")
def calculate(
    a: float = Query(..., description="First number"),
    b: float = Query(..., description="Second number"),
    operation: str = Query(
        "add",
        description="Operation: add, subtract, multiply, divide",
    ),
):
    op = operation.lower()
    if op not in OPERATIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid operation. Use one of: {', '.join(OPERATIONS)}",
        )

    if op == "divide" and b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")

    result = OPERATIONS[op](a, b)
    return {
        "a": a,
        "b": b,
        "operation": op,
        "result": result,
    }


def main():
    print("Starting server at http://127.0.0.1:8000")
    print("Examples:")
    print("  http://127.0.0.1:8000/calculate?a=10&b=5&operation=add")
    print("  http://127.0.0.1:8000/calculate?a=20&b=4&operation=divide")
    print("API docs: http://127.0.0.1:8000/docs")
    print("Press Ctrl+C to stop.\n")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
