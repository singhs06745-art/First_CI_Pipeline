def set_intersection(list1, list2):
    return sorted(set(list1) & set(list2))


if __name__ == "__main__":
    first = list(map(int, input("Enter first set numbers separated by spaces: ").split()))
    second = list(map(int, input("Enter second set numbers separated by spaces: ").split()))

    print("Intersection:", set_intersection(first, second))