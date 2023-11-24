import sys

n = int(sys.stdin.readline())

tel = [[0 for column in range(10)] for row in range(n + 1)]

for i in range(n + 1):
    for j in range(10):
        if i == 0:
            tel[i][j] = 0
        if i == 1:
            tel[i][j] = 1
        if i > 1:
            if j == 0:
                tel[i][j] = tel[i - 1][4] + tel[i - 1][6]
            if j == 1:
                tel[i][j] = tel[i - 1][6] + tel[i - 1][8]
            if j == 2:
                tel[i][j] = tel[i - 1][7] + tel[i - 1][9]
            if j == 3:
                tel[i][j] = tel[i - 1][4] + tel[i - 1][8]
            if j == 4:
                tel[i][j] = tel[i - 1][3] + tel[i - 1][9] + tel[i - 1][0]
            if j == 5:
                tel[i][j] = 0
            if j == 6:
                tel[i][j] = tel[i - 1][1] + tel[i - 1][7] + tel[i - 1][0]
            if j == 7:
                tel[i][j] = tel[i - 1][2] + tel[i - 1][6]
            if j == 8:
                tel[i][j] = tel[i - 1][1] + tel[i - 1][3]
            if j == 9:
                tel[i][j] = tel[i - 1][2] + tel[i - 1][4]

print(tel)
print((sum(tel[-1][1:8]) + tel[-1][9]) % 10 ** 9)
