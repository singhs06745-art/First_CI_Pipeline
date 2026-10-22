def find_max_min(numbers):
    if not numbers:
        return None, None

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    largest, smallest = find_max_min(numbers)

    if largest is None:
        print("The list is empty.")
    else:
        print("Maximum:", largest)
        print("Minimum:", smallest)