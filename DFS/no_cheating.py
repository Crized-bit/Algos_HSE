import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def dfs(vertex, vertex_adj, num, cut):
    num[vertex] = cut
    for n in vertex_adj[vertex]:
        if num[n] == num[vertex]:
            print('NO')
            exit(0)
        if not num[n]:
            if num[vertex] == 1:
                dfs(n, vertex_adj, num, 2)
            else:
                dfs(n, vertex_adj, num, 1)


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

    for v in range(n):
        if not num[v]:
            dfs(v, my_dict, num, 1)

    print('YES')


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()