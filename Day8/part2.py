import time

import numpy as np
from scipy.spatial.distance import pdist, squareform


def main():
    problemInput = open("inputex.txt", "r")

    points = []
    for i, line in enumerate(problemInput):
        points.append([int(v) for v in line.split(",")])
    points = np.array(points)

    distances = squareform(pdist(points))
    np.fill_diagonal(distances, np.inf)

    clusters = [[i] for i in range(len(points))]

    clusterI = -1
    clusterJ = -1
    distance = 0

    while len(clusters) > 1:
        i, j = np.unravel_index(np.argmin(distances), distances.shape)
        distance = distances[i, j]
        distances[i, j] = np.inf
        distances[j, i] = np.inf
        distances[-i, -j] = np.inf
        distances[-j, -i] = np.inf

        clusterI = -1
        clusterJ = -1
        for ci, cluster in enumerate(clusters):
            if i in cluster:
                clusterI = ci

            if j in cluster:
                clusterJ = ci

        if clusterI == clusterJ:
            continue

        if clusterI < 0 or clusterJ < 0:
            print("Value not found aborting")
            break

        copyI = clusters[clusterI]
        copyJ = clusters[clusterJ]
        clusters.remove(copyI)
        clusters.remove(copyJ)
        clusters += [copyI + copyJ]

        print(
            f"Result : {points[clusterI][0]} * {points[clusterJ][0]} = {points[clusterI][0] * points[clusterJ][0]}, distance : {distance}"
        )
        print(clusters)

    if clusterI < 0 or clusterJ < 0:
        print("Not reduced properly aborting")
        return

    print(points[clusterI])
    print(points[clusterJ])
    print(
        f"Result : {points[clusterI][0]} * {points[clusterJ][0]} = {points[clusterI][0] * points[clusterJ][0]}, distance : {distance}"
    )


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Elapsed: {end - start:.6f} seconds")
