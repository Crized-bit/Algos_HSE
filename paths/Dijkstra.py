import queue
import sys

n, s, f = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    matrix.append([*map(int, sys.stdin.readline().rstrip().split())])

to_vis = queue.Queue()
distance = [-1 for i in range(n)]

to_vis.put(s - 1)
distance[s - 1] = 0

while not to_vis.empty():
    vert = to_vis.get()
    for edge_index, edge_distance in enumerate(matrix[vert]):
        if edge_distance == 0 or edge_distance == -1:
            continue
        if (k := distance[vert] + edge_distance) < distance[edge_index] or distance[edge_index] == -1:
            to_vis.put(edge_index)
            distance[edge_index] = k
print(distance[f-1])
