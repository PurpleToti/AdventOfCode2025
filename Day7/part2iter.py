import time


def main():
    problemInput = open("input.txt", "r")
    inputDiagram = [list(line.strip()) for line in problemInput.readlines()]
    startCol = inputDiagram[0].index("S")
    splitterPossibilitiesMap = {(startCol, 0): 1}

    height = len(inputDiagram)
    width = len(inputDiagram[0])

    for row in range(height - 1):
        for col in range(width):
            if inputDiagram[row][col] == "^":
                splitterCol = col
                aboveRow = row - 1
                numPossibilities = 0

                rightPossible = splitterCol + 1 < width
                leftPossible = splitterCol - 1 >= 0

                while aboveRow >= 0:
                    if inputDiagram[aboveRow][splitterCol] == "S":
                        numPossibilities += 1

                    if inputDiagram[aboveRow][splitterCol] == "^":
                        break

                    if rightPossible:
                        if inputDiagram[aboveRow][splitterCol + 1] == "^":
                            numPossibilities += splitterPossibilitiesMap[
                                (splitterCol + 1, aboveRow)
                            ]

                    if leftPossible:
                        if inputDiagram[aboveRow][splitterCol - 1] == "^":
                            numPossibilities += splitterPossibilitiesMap[
                                (splitterCol - 1, aboveRow)
                            ]

                    aboveRow -= 1

                print(f"Num possibilities for {col}:{row} is {numPossibilities}")
                splitterPossibilitiesMap[(col, row)] = numPossibilities

    totalPossibilities = 0

    lastRow = height - 1
    for col in range(width):
        aboveRow = lastRow - 1
        numPossibilities = 0
        rightPossible = col + 1 < width
        leftPossible = col - 1 >= 0

        while aboveRow >= 0:
            if inputDiagram[aboveRow][col] == "^":
                break

            if rightPossible:
                if inputDiagram[aboveRow][col + 1] == "^":
                    numPossibilities += splitterPossibilitiesMap[(col + 1, aboveRow)]

            if leftPossible:
                if inputDiagram[aboveRow][col - 1] == "^":
                    numPossibilities += splitterPossibilitiesMap[(col - 1, aboveRow)]

            aboveRow -= 1

        totalPossibilities += numPossibilities

    print(totalPossibilities)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Elapsed: {end - start:.6f} seconds")
