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

    while True:
        nm = sys.stdin.readline().split()
        if not nm:
            break
        n, m = map(int, nm)
        my_dict = dict()
        my_dict_reversed = dict()
        visited = [0 for i in range(2 * n)]
        visited_reversed = [0 for i in range(2 * n)]

        for i in range(2 * n):
            my_dict[i] = set()
            my_dict_reversed[i] = set()

        for _ in range(m):
            a, a_bool, b, b_bool = map(int, sys.stdin.readline().rstrip().split())
            if a_bool == 1 and b_bool == 1:
                my_dict[2 * a + 1].add(2 * b)
                my_dict[2 * b + 1].add(2 * a)

                my_dict_reversed[2 * b].add(2 * a + 1)
                my_dict_reversed[2 * a].add(2 * b + 1)
            elif a_bool == 1 and b_bool == 0:
                my_dict[2 * a + 1].add(2 * b + 1)
                my_dict[2 * b].add(2 * a)

                my_dict_reversed[2 * b + 1].add(2 * a + 1)
                my_dict_reversed[2 * a].add(2 * b)
            elif a_bool == 0 and b_bool == 1:
                my_dict[2 * a].add(2 * b)
                my_dict[2 * b + 1].add(2 * a + 1)

                my_dict_reversed[2 * b].add(2 * a)
                my_dict_reversed[2 * a + 1].add(2 * b + 1)
            elif a_bool == 0 and b_bool == 0:
                my_dict[2 * a].add(2 * b + 1)
                my_dict[2 * b].add(2 * a + 1)

                my_dict_reversed[2 * b + 1].add(2 * a)
                my_dict_reversed[2 * a + 1].add(2 * b)
        # Solve
        stack = []
        paint = 1
        for v in range(2 * n):
            if not visited[v]:
                dfs(v, my_dict, visited, stack, paint)
                paint += 1

        paint = 1
        while stack:
            v = stack.pop()
            if not visited_reversed[v]:
                dfs(v, my_dict_reversed, visited_reversed, [], paint)
                paint += 1

        for i in range(n):
            if visited_reversed[2 * i] > visited_reversed[2 * i + 1]:
                print(1, end='')
            else:
                print(0, end='')
        print('')


if __name__ == '__main__':
    sys.setrecursionlimit(110000)
    threading.stack_size(200000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
