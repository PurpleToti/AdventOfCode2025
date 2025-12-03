def main():
    result = 0
    problemInput = open("input.txt", "r")
    for bank in problemInput:
        max1 = 0
        max2 = 1

        numBatteries = len(bank)
        for i in range(numBatteries - 2):
            if bank[i] > bank[max1]:
                max1 = i
                max2 = i + 1

        for j in range(max2, numBatteries - 1):
            if bank[j] > bank[max2]:
                max2 = j

        result += int(bank[max1] + bank[max2])

    print(result)


if __name__ == "__main__":
    main()
