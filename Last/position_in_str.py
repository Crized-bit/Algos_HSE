import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
final = b + '#' + a
n = len(a) + len(b) + 1
p = [0] * (n + 1)
p[0] = -1
result = []
for i in range(1, n + 1):
    k = p[i - 1]
    while k != -1 and final[k] != final[i - 1]:
        k = p[k]
    p[i] = k + 1
    if p[i] == len(b):
        result.append(i - 2 * len(b))
print(len(result))
print(*result)