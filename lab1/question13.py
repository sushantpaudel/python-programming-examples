"""Lab 1 - Question 13: Create a Pandas DataFrame for student details."""

import pandas as pd


def main():
    data = {
        "Name": ["Ravi", "Priya", "Amit", "Sneha", "Karan"],
        "Age": [20, 21, 19, 20, 22],
        "Marks": [88, 72, 91, 65, 78],
    }
    df = pd.DataFrame(data)
    print("Student DataFrame:")
    print(df)
    print(f"\nShape: {df.shape}")


if __name__ == "__main__":
    main()
