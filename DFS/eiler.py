import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def go(v, adj, max_v):
    while adj[v]:
        u = adj[v].pop()
        adj[u].remove(v)
        go(u, adj, max_v)
        if v != max_v:
            print(v + 1, end=' ')
        else:
            print()


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    my_dict = dict()
    for i in range(0, n + 1):
        my_dict[i] = set()

    for _ in range(0, m):
        a, b = map(int, sys.stdin.readline().rstrip().split())

        my_dict[a - 1].add(b - 1)
        my_dict[b - 1].add(a - 1)

    for vertex in range(n):
        if len(my_dict[vertex]) % 2 == 1:
            my_dict[vertex].add(n)
            my_dict[n].add(vertex)

    if my_dict[n]:
        print(len(my_dict[n]) // 2)
        go(n, my_dict, n)
    else:
        print(1)
        print(1, end=' ')
        go(0, my_dict, n)


if __name__ == '__main__':
    sys.setrecursionlimit(110000)
    threading.stack_size(200000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
