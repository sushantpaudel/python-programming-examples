"""Lab 1 - Question 9: NumPy array arithmetic operations."""

import numpy as np


def main():
    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])

    print("Array a:", a)
    print("Array b:", b)
    print(f"Addition:       {a + b}")
    print(f"Subtraction:    {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division:       {a / b}")


if __name__ == "__main__":
    main()
