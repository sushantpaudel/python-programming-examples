"""Lab 1 - Question 7: Function returning square and cube of a number."""

def square_and_cube(n):
    return n ** 2, n ** 3


def main():
    n = float(input("Enter a number: "))
    square, cube = square_and_cube(n)
    print(f"Square: {square}")
    print(f"Cube:   {cube}")


if __name__ == "__main__":
    main()
