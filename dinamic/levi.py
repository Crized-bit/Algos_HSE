import sys

w1 = [*sys.stdin.readline().rstrip()]
w2 = [*sys.stdin.readline().rstrip()]


def comp(i, j) -> int:
    if i == j:
        return 0
    else:
        return 1


lev = [[0 for column in range(len(w2)+1)] for row in range(len(w1)+1)]
for i in range(len(w1)+1):
    for j in range(len(w2)+1):
        if j == 0 and i == 0:
            lev[i][j] = 0
        elif j == 0:
            lev[i][j] = i
        elif i == 0:
            lev[i][j] = j
        else:
            lev[i][j] = min(lev[i - 1][j] + 1, lev[i][j - 1] + 1, lev[i - 1][j - 1] + comp(w1[i-1], w2[j-1]))
print(lev[-1][-1])
