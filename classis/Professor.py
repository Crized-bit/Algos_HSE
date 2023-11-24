"""
Sounds ez
"""
import sys
from collections import deque

N, k = sys.stdin.readline().rstrip().split()
mu_deque = deque()
mu_deque.extend(list(sys.stdin.readline().title().split()))
for i in range(int(k)):
    if len(mu_deque) == 1:
        mu_deque = [0]
        break
    if (x := int(mu_deque.popleft())) < (y := int(mu_deque.pop())):
        mu_deque.append(y)
        mu_deque.append((x + y) % (2 << 30 - 1))
    else:
        mu_deque.appendleft(x)
        mu_deque.appendleft((y - x) % (2 << 30 - 1))

print(*mu_deque)
