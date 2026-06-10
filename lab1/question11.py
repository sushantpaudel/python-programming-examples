"""Lab 1 - Question 11: Mean, median, minimum, and maximum of a NumPy array."""

import numpy as np


def main():
    arr = np.array([45, 72, 38, 91, 56, 83, 67, 49, 95, 61])
    print("Array:", arr)
    print(f"Mean:   {np.mean(arr):.2f}")
    print(f"Median: {np.median(arr):.2f}")
    print(f"Min:    {np.min(arr)}")
    print(f"Max:    {np.max(arr)}")


if __name__ == "__main__":
    main()
