import sys

b, a = map(int, sys.stdin.readline().rstrip().split())
seq = list(map(int, sys.stdin.readline().rstrip().split()))

can = [[0 for column in range(b + 1)] for row in range(a+1)]
for i in range(a + 1):
    for j in range(b + 1):

        if i == 0:
            if j == 0:
                can[i][j] = 1
            else:
                continue
        if i - 1 >= 0:
            can[i][j] = can[i - 1][j]
            if j - seq[i - 1] >= 0:
                can[i][j] = can[i][j] or can[i - 1][j - seq[i - 1]]
while not can[-1].pop():
    pass
print(len(can[-1]))
