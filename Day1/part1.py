def main():
    current = 50
    password = 0
    problemInput = open("input.txt", "r")
    for problemInputLine in problemInput:
        left = 1 - 2 * (problemInputLine[0] == "L")
        value = int(problemInputLine[1:])
        current += (left * value) % 100
        password += (current == 0) * 1

    print(password)


if __name__ == "__main__":
    main()
