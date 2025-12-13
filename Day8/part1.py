import time


def dist(p1, p2):
    return (
        (p1[0] - p2[0]) * (p1[0] - p2[0])
        + (p1[1] - p2[1]) * (p1[1] - p2[1])
        + (p1[2] - p2[2]) * (p1[2] - p2[2])
    )


def main():
    problemInput = open("input.txt", "r")
    points = []
    maxConnections = 1000
    connections = []
    clusters = {}
    for i, line in enumerate(problemInput):
        newPosition = [int(v) for v in line.split(",")]
        newPositionCluster = i

        for j, (otherPos, _) in enumerate(points):
            distance = dist(newPosition, otherPos)
            newConnection = [i, j, distance]

            enterPos = -1
            for k, connection in enumerate(connections):
                if newConnection[2] < connection[2]:
                    enterPos = k
                    break

            if len(connections) < maxConnections:
                connections.append(newConnection)

            if enterPos >= 0:
                connections = (
                    connections[:enterPos] + [newConnection] + connections[enterPos:-1]
                )

        points.append([newPosition, newPositionCluster])

    for i, (_, cluster) in enumerate(points):
        if cluster not in clusters:
            clusters[cluster] = []

        clusters[cluster].append(i)

    toConnect = connections
    toVisit = []
    while len(toConnect) > 0:
        connecting = toConnect.pop()
        cluster = connecting[0]
        toVisit.append(connecting)
        while len(toVisit) > 0:
            visiting = toVisit.pop()

            if visiting[0] not in clusters[cluster]:
                clusters[cluster].append(visiting[0])
            if visiting[1] not in clusters[cluster]:
                clusters[cluster].append(visiting[1])

            for otherConn in toConnect:
                if otherConn[0] in visiting or otherConn[1] in visiting:
                    toVisit.append(otherConn)
                    toConnect.remove(otherConn)

    clusters = sorted(clusters.values(), key=lambda x: len(x), reverse=True)
    print("Result : ", len(clusters[0]) * len(clusters[1]) * len(clusters[2]))


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Elapsed: {end - start:.6f} seconds")
