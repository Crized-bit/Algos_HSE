import math
import sys


def distance(first, second):
    if first != second:
        return (sum(((element1 - element2) ** 2 for (element1, element2) in zip(first, second)))) ** (1 / 2)
    else:
        return math.inf


n = int(sys.stdin.readline().rstrip())
points = []
for _ in range(n):
    points.append([*map(int, sys.stdin.readline().rstrip().split())])
adj = {i: set() for i in range(n)}

for i in range(n):
    for j in range(i + 1, n):
        adj[i].add((j, distance(points[i], points[j])))
        adj[j].add((i, distance(points[i], points[j])))

A = {0}
d = [distance(points[0], points[j]) for j in range(n)]
prev_index = [0 for i in range(n)]
final_distance = 0
for _ in range(n-1):
    dist = min(d)
    final_distance += dist
    vertex = d.index(dist)
    A.add(vertex)
    d[vertex] = math.inf
    for index, weight in adj[vertex]:
        if index not in A:
            if d[index] != min(d[index], weight):
                d[index] = min(d[index], weight)
                prev_index[index] = vertex

print(final_distance)
print(n-1)
for i in range(0, n-1):
    print(prev_index[i+1] + 1, i + 2)
