"""Lab 1 - Question 23: FastAPI endpoint returning student details via path parameters."""

from pathlib import Path

from fastapi import FastAPI, HTTPException
import pandas as pd
import uvicorn

DATA_FILE = Path(__file__).resolve().parent / "data" / "students.csv"

app = FastAPI(title="Lab 1 - Question 23", version="1.0")


def load_students():
    return pd.read_csv(DATA_FILE)


@app.get("/students/{name}")
def get_student(name: str):
    df = load_students()
    match = df[df["Name"].str.lower() == name.lower()]

    if match.empty:
        raise HTTPException(status_code=404, detail=f"Student '{name}' not found")

    records = match.to_dict(orient="records")
    return {"student": name, "records": records}


def main():
    print("Starting server at http://127.0.0.1:8000")
    print("Example:     http://127.0.0.1:8000/students/Ravi")
    print("API docs:    http://127.0.0.1:8000/docs")
    print("Press Ctrl+C to stop.\n")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
