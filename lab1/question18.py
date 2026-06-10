"""Lab 1 - Question 18: Line graph of student marks over time using Matplotlib."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = Path(__file__).resolve().parent / "data" / "students.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def main():
    df = pd.read_csv(DATA_FILE)
    student = "Ravi"
    student_data = df[df["Name"] == student].sort_values("Week")

    plt.figure(figsize=(8, 5))
    plt.plot(student_data["Week"], student_data["Marks"], marker="o", linewidth=2)
    plt.title(f"Marks over time — {student}")
    plt.xlabel("Week")
    plt.ylabel("Marks")
    plt.xticks(student_data["Week"])
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_file = OUTPUT_DIR / "question18_line_chart.png"
    plt.savefig(out_file)
    plt.close()
    print(f"Line chart saved to: {out_file}")


if __name__ == "__main__":
    main()
