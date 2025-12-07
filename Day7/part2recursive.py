import time

inputDiagram = [[]]


def exploreDiagram(startPos, height, width):
    currentPos = startPos
    while True:
        if currentPos[1] >= height:
            return 1

        if inputDiagram[currentPos[1]][currentPos[0]] == "^":
            toExploreR = (currentPos[0] + 1, currentPos[1])
            toExploreL = (currentPos[0] - 1, currentPos[1])

            sum = 0
            if toExploreR[0] < width:
                sum += exploreDiagram(toExploreR, height, width)

            if toExploreL[0] >= 0:
                sum += exploreDiagram(toExploreL, height, width)

            return sum

        currentPos = (currentPos[0], currentPos[1] + 1)


def main():
    global inputDiagram

    problemInput = open("inputex.txt", "r")
    inputDiagram = [list(line.strip()) for line in problemInput.readlines()]
    start = (inputDiagram[0].index("S"), 0)
    height = len(inputDiagram)
    width = len(inputDiagram[0])

    print(exploreDiagram(start, height, width))


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Elapsed: {end - start:.6f} seconds")
