import time


def main():
    problemInput = open("input.txt", "r")

    rows = [line.strip("\n") for line in problemInput.readlines() if line != ""]
    operators = rows[-1]
    rows.pop()

    rowsLength = []
    length = 0
    for c in operators:
        if c in ("*", "+"):
            if length > 0:
                rowsLength.append(length - 1)
            length = 1
        else:
            length += 1
    if length > 0:
        rowsLength.append(length)

    operators = [op for op in operators.split(" ") if op != ""]

    cols = [[[] for _ in range(length)] for length in rowsLength]
    for r in rows:
        offset = 0
        for j, rowLength in enumerate(rowsLength):
            for k in range(rowLength):
                cols[j][k].append(r[offset + k])

            offset += rowLength + 1

    numbers = []
    for i, numbersOp in enumerate(cols):
        numbers.append([])
        for j, row in enumerate(numbersOp):
            numbers[i].append(int("".join(row)))

        numbers[i] = numbers[i][::-1]
    numbers = numbers[::-1]

    operators = operators[::-1]

    result = 0
    for i, operation in enumerate(operators):
        if operation == "+":
            addition = sum(numbers[i])
            result += addition

        if operation == "*":
            multipication = 1
            for n in numbers[i]:
                multipication *= n

            result += multipication

    print(result)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Elapsed: {end - start:.6f} seconds")
