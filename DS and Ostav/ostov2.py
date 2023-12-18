import heapq
import math
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
adj = {i: set() for i in range(n)}

for _ in range(m):
    i, j, w = map(int, sys.stdin.readline().rstrip().split())
    adj[i - 1].add((j - 1, w))
    adj[j - 1].add((i - 1, w))

A = {0}
d = [math.inf] * n
Q = [(math.inf, i) for i in range(n)]
for item in adj[0]:
    Q[item[0]] = (item[1], item[0])
    d[item[0]] = item[1]
heapq.heapify(Q)

final_distance = 0
for _ in range(n - 1):
    while True:
        dist, vertex = heapq.heappop(Q)
        if vertex not in A:
            break
    final_distance += dist
    A.add(vertex)
    for index, weight in adj[vertex]:
        if index not in A:
            if d[index] != min(d[index], weight):
                d[index] = min(d[index], weight)
                heapq.heappush(Q, (d[index], index))
print(final_distance)
