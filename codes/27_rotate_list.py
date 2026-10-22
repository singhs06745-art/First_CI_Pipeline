def rotate_list(numbers, k):
    if not numbers:
        return []

    k = k % len(numbers)
    return numbers[-k:] + numbers[:-k] if k else numbers.copy()


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter rotation count: "))

    print("Rotated list:", rotate_list(numbers, k))