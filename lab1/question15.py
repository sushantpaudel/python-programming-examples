"""Lab 1 - Question 15: Handle missing values using Pandas (fill or drop)."""

import pandas as pd
import numpy as np


def main():
    data = {
        "Name": ["Ravi", "Priya", "Amit", "Sneha", "Karan"],
        "Age": [20, 21, np.nan, 20, 22],
        "Marks": [88, np.nan, 91, 65, 78],
    }
    df = pd.DataFrame(data)

    print("Original DataFrame (with missing values):")
    print(df)
    print()

    filled = df.fillna({"Age": df["Age"].mean(), "Marks": df["Marks"].mean()})
    print("After fillna (mean for Age and Marks):")
    print(filled.round(2))
    print()

    dropped = df.dropna()
    print("After dropna (rows with any missing value removed):")
    print(dropped)


if __name__ == "__main__":
    main()
