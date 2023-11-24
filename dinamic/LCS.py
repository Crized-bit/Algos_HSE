import sys

a = int(sys.stdin.readline())
seq1 = list(map(int, sys.stdin.readline().rstrip().split()))
b = int(sys.stdin.readline())
seq2 = list(map(int, sys.stdin.readline().rstrip().split()))

LCS = [[0 for column in range(b)] for row in range(a)]

for i in range(a):
    for j in range(b):
        if i - 1 >= 0:
            LCS[i][j] = max(LCS[i][j], LCS[i - 1][j])
        if j - 1 >= 0:
            LCS[i][j] = max(LCS[i][j], LCS[i][j - 1])
        if seq1[i] == seq2[j]:
            if j - 1 >= 0 and i - 1 >= 0:
                LCS[i][j] = max(LCS[i][j], LCS[i - 1][j - 1] + 1)
            else:
                LCS[i][j] = max(LCS[i][j], 1)
print(LCS[-1][-1])
