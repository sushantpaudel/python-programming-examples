"""Lab 1 - Question 24: FastAPI endpoint using query parameters."""

from fastapi import FastAPI, Query
import uvicorn

app = FastAPI(title="Lab 1 - Question 24", version="1.0")


@app.get("/greet")
def greet(
    name: str = Query(..., description="Name of the person"),
    course: str = Query("Generative AI", description="Course name"),
):
    return {
        "message": f"Hello, {name}!",
        "course": course,
        "info": f"You are enrolled in {course}.",
    }


@app.get("/filter-marks")
def filter_marks(
    min_marks: int = Query(75, ge=0, le=100, description="Minimum marks"),
    max_marks: int = Query(100, ge=0, le=100, description="Maximum marks"),
):
    return {
        "min_marks": min_marks,
        "max_marks": max_marks,
        "message": f"Filtering students with marks between {min_marks} and {max_marks}",
    }


def main():
    print("Starting server at http://127.0.0.1:8000")
    print("Examples:")
    print("  http://127.0.0.1:8000/greet?name=Priya&course=Generative%20AI")
    print("  http://127.0.0.1:8000/filter-marks?min_marks=70&max_marks=90")
    print("API docs: http://127.0.0.1:8000/docs")
    print("Press Ctrl+C to stop.\n")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
