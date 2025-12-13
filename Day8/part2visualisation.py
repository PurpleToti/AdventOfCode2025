import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import pdist, squareform

# Load data
points = []
with open("inputex.txt", "r") as f:
    for line in f:
        points.append([int(v) for v in line.split(",")])
points = np.array(points)


# Run clustering algorithm and store steps
def get_clustering_steps():
    distances = squareform(pdist(points))
    np.fill_diagonal(distances, np.inf)

    clusters = [[i] for i in range(len(points))]
    steps = []
    connections = []

    # Store initial state
    steps.append(
        {"connections": [], "clusters": [cluster.copy() for cluster in clusters]}
    )

    while len(clusters) > 1:
        i, j = np.unravel_index(np.argmin(distances), distances.shape)
        distance = distances[i, j]
        distances[i, j] = np.inf
        distances[j, i] = np.inf

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
            break

        # Store connection
        connections.append((i, j, distance))

        # Store step
        steps.append(
            {
                "connections": connections.copy(),
                "clusters": [cluster.copy() for cluster in clusters],
                "latest": (i, j),
            }
        )

        copyI = clusters[clusterI]
        copyJ = clusters[clusterJ]
        clusters.remove(copyI)
        clusters.remove(copyJ)
        clusters += [copyI + copyJ]

    return steps


# Get all steps
steps = get_clustering_steps()

# Create animation
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")


def animate(frame):
    ax.clear()

    if frame >= len(steps):
        frame = len(steps) - 1

    step = steps[frame]

    # Plot points
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c="blue", s=100)

    # Draw existing connections
    for i, j, dist in step["connections"]:
        ax.plot(
            [points[i, 0], points[j, 0]],
            [points[i, 1], points[j, 1]],
            [points[i, 2], points[j, 2]],
            "r-",
            alpha=0.6,
            linewidth=2,
        )

    # Highlight latest connection
    if "latest" in step:
        i, j = step["latest"]
        ax.plot(
            [points[i, 0], points[j, 0]],
            [points[i, 1], points[j, 1]],
            [points[i, 2], points[j, 2]],
            "y-",
            alpha=1.0,
            linewidth=4,
        )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"Hierarchical Clustering - Step {frame + 1}/{len(steps)}")


# Create and run animation
anim = animation.FuncAnimation(
    fig, animate, frames=len(steps), interval=1500, repeat=True
)
plt.show()
