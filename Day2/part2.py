import time


def main():
    result = 0
    problemInput = open("input.txt", "r")
    problemLine = problemInput.readline().strip()
    ranges = problemLine.split(",")

    for r in ranges:
        start, end = r.split("-")
        if start[0] == "0" or end[0] == "0":
            continue

        start, end = int(start), int(end)
        for number in range(start, end + 1):
            strNumber = str(number)
            strNumberLen = len(strNumber)
            for i in range(1, strNumberLen // 2 + 1):
                if strNumberLen % i != 0:
                    continue

                if int(strNumber[:i] * (strNumberLen // i)) == number:
                    result += number
                    break

    print(result)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Elapsed: {end - start:.6f} seconds")
