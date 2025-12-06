import time


def main():
    problemInput = open("input.txt", "r")
    diagram = [line.strip() for line in problemInput.readlines()]
    height = len(diagram)
    width = len(diagram[0])

    numValidRolls = 0
    for y in range(height):
        for x in range(width):
            cell = diagram[y][x]

            if cell == "@":
                numRolls = 0

                for dx, dy in (
                    (0, 1),
                    (1, 1),
                    (1, 0),
                    (-1, 1),
                    (-1, 0),
                    (-1, -1),
                    (0, -1),
                    (1, -1),
                ):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        if diagram[ny][nx] == "@":
                            numRolls += 1

                if numRolls < 4:
                    numValidRolls += 1

    print(numValidRolls)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Elapsed: {end - start:.6f} seconds")
