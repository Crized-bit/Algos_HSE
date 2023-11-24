import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def dfs(vertex, vertex_adj, visited, stack, paint):
    visited[vertex] = paint
    for n in vertex_adj[vertex]:
        if not visited[n]:
            dfs(n, vertex_adj, visited, stack, paint)
    stack.append(vertex)


def main():
    # Input
    n, m = map(int, sys.stdin.readline().rstrip().split())
    my_dict = dict()
    my_dict_reversed = dict()
    visited = [0 for i in range(n)]
    visited_reversed = [0 for i in range(n)]
    for i in range(0, n):
        my_dict[i] = set()
        my_dict_reversed[i] = set()

    for _ in range(0, m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if a == b:
            continue
        my_dict[a - 1].add(b - 1)
        my_dict_reversed[b - 1].add(a - 1)

    # Solve
    stack = []
    paint = 1
    for v in range(n):
        if not visited[v]:
            dfs(v, my_dict, visited, stack, paint)
            paint += 1

    paint = 1
    while stack:
        v = stack.pop()
        if not visited_reversed[v]:
            dfs(v, my_dict_reversed, visited_reversed, [], paint)
            paint += 1

    result_set = set()
    for node, neighbors in my_dict.items():
        for neighbor in neighbors:
            if visited_reversed[node] != visited_reversed[neighbor]:
                result_set.add((visited_reversed[node], visited_reversed[neighbor]))
    print(len(result_set))

if __name__ == '__main__':
    sys.setrecursionlimit(110000)
    threading.stack_size(200000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
