import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
seq1 = [list(map(int, sys.stdin.readline().rstrip().split()))]
for _ in range(n - 1):
    seq1.append(list(map(int, sys.stdin.readline().rstrip().split())))

path = [[10**9 for column in range(m)] for row in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            path[i][j] = seq1[i][j]
            continue
        if i >= 1:
            path[i][j] = min(path[i][j], path[i - 1][j])
        if j >= 1:
            path[i][j] = min(path[i][j], path[i][j - 1])
        path[i][j] += seq1[i][j]
print(path[-1][-1])