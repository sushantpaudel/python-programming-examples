"""Lab 1 - Question 10: Reshape a 1D NumPy array into 2D (3×4 and 4×3)."""

import numpy as np


def main():
    arr_1d = np.arange(1, 13)
    print("Original 1D array:")
    print(arr_1d)
    print(f"Shape: {arr_1d.shape}\n")

    arr_3x4 = arr_1d.reshape(3, 4)
    print("Reshaped to 3×4:")
    print(arr_3x4)
    print(f"Shape: {arr_3x4.shape}\n")

    arr_4x3 = arr_1d.reshape(4, 3)
    print("Reshaped to 4×3:")
    print(arr_4x3)
    print(f"Shape: {arr_4x3.shape}")


if __name__ == "__main__":
    main()
