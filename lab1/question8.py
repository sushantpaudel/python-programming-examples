"""Lab 1 - Question 8: Sum and average of a list using a function."""

def sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average


def main():
    raw = input("Enter numbers separated by spaces: ")
    numbers = [float(x) for x in raw.split()]

    if not numbers:
        print("No numbers entered.")
        return

    total, average = sum_and_average(numbers)
    print(f"Numbers: {numbers}")
    print(f"Sum:     {total}")
    print(f"Average: {average}")


if __name__ == "__main__":
    main()
