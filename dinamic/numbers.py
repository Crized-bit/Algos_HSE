import sys

a = int(sys.stdin.readline())

LCS = [[0 for column in range(10)] for row in range(a + 1)]

for i in range(1, a + 1):
    for j in range(10):
        if i == 0:
            LCS[i][j] = 0
        if i == 1:
            LCS[i][j] = 1
        if i >= 1:
            LCS[i][j] += LCS[i - 1][j]
            if j >= 1:
                LCS[i][j] += LCS[i - 1][j - 1]
            if j < 9:
                LCS[i][j] += LCS[i - 1][j + 1]

print(sum(LCS[-1][1:]))
