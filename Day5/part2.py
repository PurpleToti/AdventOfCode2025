def main():
    problemInput = open("input.txt", "r")

    ranges = []
    while True:
        inputLine = problemInput.readline().strip()

        if inputLine == "":
            break

        rangeStart, rangeEnd = [int(elt) for elt in inputLine.split("-")]
        ranges.append([rangeStart, rangeEnd])

    uniqueRanges = []
    while True:
        uniqueRanges = []
        for rangeStart, rangeEnd in ranges:
            for i, (uniqueRangeStart, uniqueRangeEnd) in enumerate(uniqueRanges):
                if (
                    uniqueRangeStart <= rangeStart <= uniqueRangeEnd
                    and uniqueRangeStart <= rangeEnd <= uniqueRangeEnd
                ):
                    break

                if (
                    uniqueRangeStart <= rangeStart <= uniqueRangeEnd
                    and uniqueRangeEnd <= rangeEnd
                ):
                    uniqueRanges[i][1] = rangeEnd
                    break

                if (
                    uniqueRangeStart <= rangeEnd <= uniqueRangeEnd
                    and rangeStart <= uniqueRangeStart
                ):
                    uniqueRanges[i][0] = rangeStart
                    break

                if (
                    rangeStart <= uniqueRangeStart <= rangeEnd
                    and rangeStart <= uniqueRangeEnd <= rangeEnd
                ):
                    uniqueRanges[i][0] = rangeStart
                    uniqueRanges[i][1] = rangeEnd
                    break
            else:
                uniqueRanges.append([rangeStart, rangeEnd])

        if ranges == uniqueRanges:
            break

        ranges = [[elt[0], elt[1]] for elt in uniqueRanges]

    numValidNumbers = 0
    for rangeStart, rangeEnd in uniqueRanges:
        numValidNumbers += rangeEnd - rangeStart + 1

    print(numValidNumbers)


if __name__ == "__main__":
    main()
