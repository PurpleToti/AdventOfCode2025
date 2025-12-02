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
        for n in range(start, end + 1):
            strNumber = str(n)
            strNumberLen = len(strNumber)
            if strNumberLen % 2 == 1:
                continue

            halfSize = strNumberLen // 2
            if strNumber[:halfSize] == strNumber[halfSize:]:
                result += n

    print(result)


if __name__ == "__main__":
    main()
