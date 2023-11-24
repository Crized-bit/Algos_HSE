import sys
import math

initial = sys.stdin.readline().rstrip()
n = len(initial)
dp = [[0 for column in range(n)] for row in range(n)]

for right_br in range(n):
    for left_br in range(right_br, -1, -1):
        if left_br == right_br:
            dp[right_br][left_br] = 1
        else:
            minim = math.inf
            rnd = initial[left_br] == '(' and initial[right_br] == ')'
            sq = initial[left_br] == '[' and initial[right_br] == ']'
            fig = initial[left_br] == '{' and initial[right_br] == '}'

            if rnd or sq or fig:
                minim = dp[left_br + 1][right_br - 1]

            for i in range(left_br, right_br):
                minim = min(minim, dp[left_br][i] + dp[i + 1][right_br])

            dp[left_br][right_br] = minim
first_ans = 0
print(n - dp[0][n-1])
