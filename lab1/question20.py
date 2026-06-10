"""Lab 1 - Question 20: Histogram to visualize distribution of marks."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = Path(__file__).resolve().parent / "data" / "students.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def main():
    df = pd.read_csv(DATA_FILE)

    plt.figure(figsize=(8, 5))
    plt.hist(df["Marks"], bins=8, color="coral", edgecolor="black", alpha=0.8)
    plt.title("Distribution of student marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.tight_layout()

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_file = OUTPUT_DIR / "question20_histogram.png"
    plt.savefig(out_file)
    plt.close()
    print(f"Histogram saved to: {out_file}")


if __name__ == "__main__":
    main()
