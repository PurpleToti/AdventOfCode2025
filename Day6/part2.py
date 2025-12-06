import time


def main():
    problemInput = open("input.txt", "r")

    lines = [line.strip("\n") for line in problemInput.readlines() if line != ""]
    height = len(lines)
    width = len(lines[0])

    result = 0
    numbersInOp = []
    for numCol in range(width - 1, -1, -1):
        col = ""
        for numRow in range(0, height):
            col += lines[numRow][numCol]
        col = col.strip()

        if col == "":
            continue

        if col[-1] in ("*", "+"):
            numbersInOp.append(int(col[:-1]))

            if col[-1] == "+":
                addition = sum(numbersInOp)
                result += addition

            if col[-1] == "*":
                multipication = 1
                for n in numbersInOp:
                    multipication *= n

                result += multipication

            numbersInOp = []
        else:
            numbersInOp.append(int(col))

    print(result)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Elapsed: {end - start:.6f} seconds")
