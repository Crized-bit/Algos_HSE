import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
c = list(map(int, sys.stdin.readline().rstrip().split()))

cost = [[-999999 for column in range(b + 1)] for row in range(a + 1)]
for i in range(0, a + 1):
    for j in range(b + 1):

        if i == 0:
            if j == 0:
                cost[i][j] = 0
            else:
                continue
        if i - 1 >= 0:
            cost[i][j] = cost[i - 1][j]
            if j - seq[i - 1] >= 0:
                cost[i][j] = max(cost[i][j], cost[i - 1][j - seq[i - 1]] + c[i - 1])
max_cost = max(cost[-1])
items = []
for i in range(a):
    index = cost[-1 - i].index(max_cost)
    if cost[-1 - i][index] == cost[-2 - i][index]:
        continue
    prew_cost = max_cost - c[-1 - i]
    index = cost[-2 - i].index(prew_cost)
    items.append(a - i)
    max_cost = prew_cost
print(len(items))
print(*reversed(items))

