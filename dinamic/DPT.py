import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * n
dp[0] = 1
dp_sub = [[number] for number in a]
for i in range(1, n):
    tmp_arr = []
    for j in range(i):
        if a[i] > a[j]:
            dp_tmp = max(dp[i], dp[j])
            if dp_tmp > dp[i]:
                dp[i] = dp_tmp
                tmp_arr = dp_sub[j].copy()
    dp[i] += 1
    tmp_arr.append(a[i])
    dp_sub[i] = [*tmp_arr]
print(max(dp))
print(*dp_sub[dp.index(max(dp))])