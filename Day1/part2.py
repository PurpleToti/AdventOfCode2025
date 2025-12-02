def main():
    current = 50
    password = 0
    problemInput = open("input.txt", "r")
    for problemInputLine in problemInput:
        left = 1 - 2 * (problemInputLine[0] == "L")
        value = int(problemInputLine[1:])
        current = current + value * left
        zeros = (current // 100) * left
        current = current % 100
        password += zeros

    print(password)


if __name__ == "__main__":
    main()
