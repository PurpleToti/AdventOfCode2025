def main():
    problemInput = open("input.txt", "r")

    ranges = []
    while True:
        inputLine = problemInput.readline().strip()

        if inputLine == "":
            break

        rangeStart, rangeEnd = [int(elt) for elt in inputLine.split("-")]
        ranges.append((rangeStart, rangeEnd))

    print(
        "\n".join(
            str(rangeStart) + "-" + str(rangeEnd) for rangeStart, rangeEnd in ranges
        )
    )

    numValidProducts = 0
    while True:
        inputLine = problemInput.readline().strip()

        if inputLine == "":
            break

        productNumber = int(inputLine)

        for rangeStart, rangeEnd in ranges:
            if rangeStart <= productNumber <= rangeEnd:
                numValidProducts += 1
                break

    print(numValidProducts)


if __name__ == "__main__":
    main()
