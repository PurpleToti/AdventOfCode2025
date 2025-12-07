import time


def main():
    problemInput = open("input.txt", "r")
    inputDiagram = [list(line.strip()) for line in problemInput.readlines()]
    start = (inputDiagram[0].index("S"), 0)
    height = len(inputDiagram)
    width = len(inputDiagram[0])

    toVisit = set()
    visited = set()
    toVisit.add(start)

    totalSpliters = 0

    while len(toVisit) != 0:
        visiting = toVisit.pop()
        visited.add(visiting)

        if (0 > visiting[0] or visiting[0] >= width) or (
            0 > visiting[1] or visiting[1] >= height
        ):
            continue

        if inputDiagram[visiting[1]][visiting[0]] == ".":
            inputDiagram[visiting[1]][visiting[0]] = "|"

        belowCol, belowRow = visiting[0], visiting[1] + 1

        if belowRow >= height:
            continue

        belowSymbol = inputDiagram[belowRow][belowCol]

        if belowSymbol == ".":
            newToVisit = (belowCol, belowRow)
            if newToVisit not in visited:
                toVisit.add(newToVisit)
        elif belowSymbol == "^":
            totalSpliters += 1

            newToVisit = (belowCol + 1, belowRow)
            if newToVisit not in visited:
                toVisit.add(newToVisit)

            newToVisit = (belowCol - 1, belowRow)
            if newToVisit not in visited:
                toVisit.add(newToVisit)

    print(totalSpliters)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Elapsed: {end - start:.6f} seconds")
