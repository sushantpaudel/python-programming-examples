#!/usr/bin/env python3
"""CLI to list and run lab question scripts."""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

LABS = {
    "lab1": {
        "title": "Lab 1 — Python, NumPy, Pandas, Matplotlib & FastAPI",
        "questions": {
            1: "Arithmetic on two numbers",
            2: "Even or odd check",
            3: "Largest of three numbers",
            4: "Numbers 1–20 (for loop)",
            5: "Numbers 1–10 (while loop)",
            6: "Calculator using functions",
            7: "Square and cube of a number",
            8: "Sum and average of a list",
            9: "NumPy array arithmetic",
            10: "Reshape 1D array to 2D",
            11: "NumPy mean, median, min, max",
            12: "Generate 10 random numbers (NumPy)",
            13: "Pandas DataFrame — student details",
            14: "Filter students (marks > 75)",
            15: "Handle missing values (Pandas)",
            16: "GroupBy — average marks by category",
            17: "Read CSV — first 5 rows",
            18: "Line graph — marks over time",
            19: "Bar chart — five students",
            20: "Histogram — marks distribution",
            21: "Pie chart — grade distribution",
            22: "FastAPI — welcome endpoint",
            23: "FastAPI — student path parameters",
            24: "FastAPI — query parameters",
            25: "FastAPI — calculator API",
        },
    },
}

# Questions that start a web server (run one at a time; press Ctrl+C to stop)
API_QUESTIONS = {22, 23, 24, 25}


def question_path(lab: str, number: int) -> Path:
    path = ROOT / lab / f"question{number}.py"
    if not path.is_file():
        raise FileNotFoundError(f"Not found: {path.relative_to(ROOT)}")
    return path


def list_questions(lab: str) -> None:
    info = LABS[lab]
    print(f"\n{info['title']} ({lab}/)\n")
    for num, desc in sorted(info["questions"].items()):
        print(f"  {num:2d}. {desc}  →  {lab}/question{num}.py")
    print()


def run_question(lab: str, number: int) -> int:
    path = question_path(lab, number)
    desc = LABS[lab]["questions"].get(number, "")
    print(f"\n{'=' * 60}")
    print(f"Running {lab}/question{number}.py — {desc}")
    print(f"{'=' * 60}\n")
    if number in API_QUESTIONS:
        print("Note: This starts a web server on http://127.0.0.1:8000")
        print("      Open /docs in your browser. Press Ctrl+C to stop.\n")
    result = subprocess.run([sys.executable, str(path)], cwd=ROOT)
    return result.returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run Generative AI lab question scripts.",
        epilog="Examples:\n"
        "  python lab_cli.py list\n"
        "  python lab_cli.py run 1\n"
        "  python lab_cli.py run 1 3 5\n"
        "  python lab_cli.py run --lab lab1 2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    list_p = sub.add_parser("list", help="List available questions")
    list_p.add_argument(
        "--lab",
        default="lab1",
        choices=LABS.keys(),
        help="Lab folder name (default: lab1)",
    )

    run_p = sub.add_parser("run", help="Run one or more questions")
    run_p.add_argument(
        "numbers",
        type=int,
        nargs="+",
        metavar="N",
        help="Question number(s), e.g. 1 or 1 2 3",
    )
    run_p.add_argument(
        "--lab",
        default="lab1",
        choices=LABS.keys(),
        help="Lab folder name (default: lab1)",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "list":
        list_questions(args.lab)
        return 0

    if args.command == "run":
        exit_code = 0
        for num in args.numbers:
            if num not in LABS[args.lab]["questions"]:
                print(f"Error: question {num} is not available in {args.lab}.", file=sys.stderr)
                exit_code = 1
                continue
            code = run_question(args.lab, num)
            if code != 0:
                exit_code = code
        return exit_code

    return 0


if __name__ == "__main__":
    sys.exit(main())
