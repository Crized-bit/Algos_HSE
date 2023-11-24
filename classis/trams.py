"""
Once again dunno what to do, instead of N iterations in worst case
"""
import bisect
import sys

# Get Data
N_countries = int(sys.stdin.readline().rstrip())
data = list(sys.stdin.readline().rstrip().split())
data = [(int(val), i) for i, val in enumerate(data)]

data.sort()
N_questions = int(input())
for i in range(N_questions):
    first_city, second_city, value = sys.stdin.readline().rstrip().split()
    print(int(bisect.bisect_left(data, (int(value), int(first_city) - 1)) != bisect.bisect_right(data, (
        int(value), int(second_city) - 1))),
          end='')
