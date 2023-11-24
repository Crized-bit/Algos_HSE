import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def dfs(vertex, vertex_adj, num, cut):
    num[vertex] = cut + 1
    for n in vertex_adj[vertex]:
        if not num[n]:
            dfs(n, vertex_adj, num, cut)


def main():
    # Input
    n, m = map(int, sys.stdin.readline().rstrip().split())
    my_dict = dict()
    num = [0 for i in range(n)]

    for i in range(0, n):
        my_dict[i] = set()
    for _ in range(0, m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        my_dict[a - 1].add(b - 1)
        my_dict[b - 1].add(a - 1)

    # Solve
    cut = 0
    for v in range(n):
        if not num[v]:
            dfs(v, my_dict, num, cut)
            cut += 1
    print(cut)
    print(*num)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
