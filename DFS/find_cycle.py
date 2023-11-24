import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def dfs(vertex, vertex_adj, num, cut, res_array):
    num[vertex] = cut
    for n in vertex_adj[vertex]:
        if num[vertex] == num[n]:
            print('YES')
            res_array.append(vertex + 1)
            return n + 1
        if not num[n]:
            flag = dfs(n, vertex_adj, num, cut, res_array)
            if flag:
                if vertex + 1 != flag:
                    res_array.append(vertex + 1)
                    return flag
                else:
                    res_array.append(vertex + 1)
                    print(*reversed(res_array))
                    exit(0)
    num[vertex] = -cut
    return 0


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

    # Solve
    flag = 0
    res_array = []
    for v in range(n):
        if not num[v]:
            flag = dfs(v, my_dict, num, v + 1, res_array)

    if not flag:
        print('NO')


if __name__ == '__main__':
    sys.setrecursionlimit(110000)
    threading.stack_size(200000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()