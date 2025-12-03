def main():
    result = 0
    problemInput = open("input.txt", "r")
    numToPower = 12
    for bank in problemInput:
        maxs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        numBatteries = len(bank)
        for i in range(numToPower):
            limit = i - numToPower
            for j in range(maxs[i], (numBatteries) + limit):
                if bank[j] > bank[maxs[i]]:
                    maxs[i] = j

            maxs[i + 1] = maxs[i] + 1

        bankResult = int("".join([bank[i] for i in maxs[:-1]]))
        result += bankResult

    print(result)


if __name__ == "__main__":
    main()
