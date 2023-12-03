import queue
import sys

n = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(n):
    matrix.append([*map(int, sys.stdin.readline().rstrip().split())])

max_dist = [0 for i in range(n)]
to_vis = queue.Queue()
for vertex in range(n):
    distance = [-1 for j in range(n)]

    to_vis.put(vertex - 1)
    distance[vertex - 1] = 0

    while not to_vis.empty():
        vert = to_vis.get()
        for edge_index, edge_distance in enumerate(matrix[vert]):
            if edge_distance == 0 or edge_distance == -1:
                continue
            if (k := distance[vert] + edge_distance) < distance[edge_index] or distance[edge_index] == -1:
                to_vis.put(edge_index)
                distance[edge_index] = k
    max_dist[vertex] = max(distance)

print(max(max_dist))
print(min(max_dist))
