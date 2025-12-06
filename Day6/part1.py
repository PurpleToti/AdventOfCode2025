import time


def main():
    problemInput = open("input.txt", "r")

    inputLine = problemInput.readline().strip()
    lineNumbers = [int(n) for n in inputLine.split(" ") if n != ""]

    numbers = []
    for i, lineNumber in enumerate(lineNumbers):
        numbers.append([])
        numbers[i].append(lineNumber)

    while True:
        inputLine = problemInput.readline().strip()
        elements = [elt for elt in inputLine.split(" ") if elt != ""]

        if not elements[0].isdigit():
            break

        lineNumbers = [int(n) for n in elements]

        for i, lineNumber in enumerate(lineNumbers):
            numbers[i].append(lineNumber)

    result = 0
    for i, operation in enumerate(elements):
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
