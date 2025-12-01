def main():
    current = 50
    password = 0
    with open("input.txt", "r") as problemInput:
        for problemInputLine in problemInput:
            direction = problemInputLine[0]
            value = int(problemInputLine[1:].strip())
            if direction == "L":
                value = -value

            current = (current + value) % 100

            if current == 0:
                password += 1

    print(password)


if __name__ == "__main__":
    main()
