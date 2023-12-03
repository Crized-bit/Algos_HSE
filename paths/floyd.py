import sys
import math

n, m, k = map(int, sys.stdin.readline().rstrip().split())

matrix = [[-math.inf for i in range(n)] for x in range(n)]
prev = [[j for j in range(n)] for s in range(n)]
edges = []
for i in range(n):
    matrix[i][i] = 0
for m in range(m):
    in_, out_, len_ = map(int, sys.stdin.readline().rstrip().split())
    edges.append(hash((in_-1, out_-1)))
    matrix[in_ - 1][out_ - 1] = len_

for i in range(n):
    for u in range(n):
        for v in range(n):
            if matrix[u][i] + matrix[i][v] > matrix[u][v]:
                matrix[u][v] = matrix[u][i] + matrix[i][v]
                prev[u][v] = prev[u][i]

city = [*map(int, sys.stdin.readline().rstrip().split())]

result_city = []
for i in range(k - 1):
    u, v = city[i] - 1, city[i + 1] - 1
    c = u
    while c != v:
        if matrix[c][c] > 0:
            print('infinitely kind')
            exit(0)
        result_city.append(c)
        c = prev[c][v]
    if matrix[v][v] > 0:
        print('infinitely kind')
        exit(0)
result_city.append(v)

print(len(result_city) - 1)
for i in range(len(result_city) - 1):
    print(edges.index(hash((result_city[i], result_city[i + 1])))+1, end=' ')
