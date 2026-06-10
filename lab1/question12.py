"""Lab 1 - Question 12: Generate 10 random numbers using NumPy."""

import numpy as np


def main():
    rng = np.random.default_rng(seed=42)
    numbers = rng.integers(1, 101, size=10)
    print("10 random numbers (1–100):")
    print(numbers)


if __name__ == "__main__":
    main()
