import sys

sys.stdin.readline()
a = sys.stdin.readline().rstrip().split()
n = len(a)
z = [0] * (n)
z[0] = 0
l, r = 0, -1
result = []
for i in range(n):
    if i > r:
        k = 0
    else:
        k = min(z[l + r - i + 1], r - i + 1)
    while i + k < n and i - k - 1 >= 0 and a[i + k] == a[i - k - 1]:
        k += 1
    z[i] = k
    if i + k - 1 > r:
        l = i - k
        r = i + k - 1

for i in range(n // 2 + 1):
    if z[i] != 0 and z[i] == i:
        result.append(n - z[i])
result.append(n)
print(*result)
