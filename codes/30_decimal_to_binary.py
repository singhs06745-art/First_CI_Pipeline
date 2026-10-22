def decimal_to_binary(number):
    if number == 0:
        return "0"

    sign = "-" if number < 0 else ""
    number = abs(number)
    binary = ""

    while number > 0:
        binary = str(number % 2) + binary
        number //= 2

    return sign + binary


if __name__ == "__main__":
    number = int(input("Enter a decimal number: "))
    print("Binary:", decimal_to_binary(number))