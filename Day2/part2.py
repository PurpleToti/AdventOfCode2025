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
                for j in range(1, strNumberLen // i):
                    if strNumber[j * i : j * i + i] != strNumber[:i]:
                        break
                else:
                    result += number
                    break

    print(result)


if __name__ == "__main__":
    main()
