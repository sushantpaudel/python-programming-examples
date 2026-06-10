# Generative AI — Python Lab Implementation

Lab solutions organized by folder (`lab1/`). Each question is a separate file: `question1.py` … `question25.py`.

## Prerequisites

- Python 3.9 or newer (`python3 --version`)

## 1. Create and activate a virtual environment

From the project root (`python-implementation/`):

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt)**

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Windows (PowerShell)**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

You should see `(venv)` in your terminal prompt when the environment is active.

## 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

| Questions | Packages needed |
|-----------|-----------------|
| 1–8 | Standard library only |
| 9–12 | NumPy |
| 13–17 | NumPy, Pandas |
| 18–21 | NumPy, Pandas, Matplotlib |
| 22–25 | FastAPI, Uvicorn |

Plots from questions **18–21** are saved under `lab1/output/`.

## 3. Run questions

### Option A — CLI (recommended)

```bash
python lab_cli.py list
python lab_cli.py run 1
python lab_cli.py run 11 12 13
```

Run all non-API questions:

```bash
python lab_cli.py run 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
```

### Option B — Run a file directly

```bash
python lab1/question17.py
```

### FastAPI questions (22–25)

These start a **web server** on `http://127.0.0.1:8000`. Run **one at a time**; press **Ctrl+C** to stop before starting the next.

```bash
python lab_cli.py run 22
# Browser: http://127.0.0.1:8000  |  Docs: http://127.0.0.1:8000/docs
```

| # | Try in browser |
|---|----------------|
| 22 | `http://127.0.0.1:8000/` |
| 23 | `http://127.0.0.1:8000/students/Ravi` |
| 24 | `http://127.0.0.1:8000/greet?name=Priya&course=Generative%20AI` |
| 25 | `http://127.0.0.1:8000/calculate?a=10&b=5&operation=add` |

## Lab 1 — All 25 questions

| # | Topic | File |
|---|--------|------|
| 1 | Addition, subtraction, multiplication, division | `lab1/question1.py` |
| 2 | Even or odd | `lab1/question2.py` |
| 3 | Largest of three numbers | `lab1/question3.py` |
| 4 | Numbers 1–20 (`for` loop) | `lab1/question4.py` |
| 5 | Numbers 1–10 (`while` loop) | `lab1/question5.py` |
| 6 | Calculator using functions | `lab1/question6.py` |
| 7 | Square and cube of a number | `lab1/question7.py` |
| 8 | Sum and average of a list | `lab1/question8.py` |
| 9 | NumPy array arithmetic | `lab1/question9.py` |
| 10 | Reshape 1D array to 2D (3×4, 4×3) | `lab1/question10.py` |
| 11 | Mean, median, min, max (NumPy) | `lab1/question11.py` |
| 12 | 10 random numbers (NumPy) | `lab1/question12.py` |
| 13 | Pandas DataFrame — student details | `lab1/question13.py` |
| 14 | Filter students (marks > 75) | `lab1/question14.py` |
| 15 | Handle missing values (fill / drop) | `lab1/question15.py` |
| 16 | GroupBy — average marks by category | `lab1/question16.py` |
| 17 | Read CSV — first 5 rows | `lab1/question17.py` |
| 18 | Line graph — marks over time | `lab1/question18.py` |
| 19 | Bar chart — five students | `lab1/question19.py` |
| 20 | Histogram — marks distribution | `lab1/question20.py` |
| 21 | Pie chart — grade distribution | `lab1/question21.py` |
| 22 | FastAPI — welcome message | `lab1/question22.py` |
| 23 | FastAPI — student details (path params) | `lab1/question23.py` |
| 24 | FastAPI — query parameters | `lab1/question24.py` |
| 25 | FastAPI — calculator API | `lab1/question25.py` |

**Shared data:** `lab1/data/students.csv`

## Deactivate the virtual environment

```bash
deactivate
```

## Project layout

```
python-implementation/
├── README.md
├── requirements.txt
├── lab_cli.py
├── venv/
└── lab1/
    ├── data/
    │   └── students.csv
    ├── output/              # charts from Q18–21
    ├── question1.py … question25.py
    └── …
```
