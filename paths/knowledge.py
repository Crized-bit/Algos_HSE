import math
import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_dict = dict()
    visited_dfs = [0 for i in range(n)]
    for i in range(n):
        adj_dict.update({i: set()})
    for _ in range(m):
        in_, out_, len_ = map(int, sys.stdin.readline().rstrip().split())
        adj_dict[out_ - 1].add((in_ - 1, len_))

    distance_iter = [-math.inf] * n
    distance_iter[0] = 0
    k = 0
    cycle = False
    indices = set()

    def dfs(vertex_initial, vertex_to_find):
        neighbors = adj_dict[vertex_initial]
        visited_dfs[vertex_initial] = 1
        cycle_flag = False
        for neighbor, _ in neighbors:
            if vertex_to_find == neighbor:
                cycle_flag = True
                break
            if visited_dfs[neighbor] == 0:
                cycle_flag = dfs(neighbor, vertex_to_find) or cycle_flag
                if cycle_flag:
                    break
        return cycle_flag

    while True:
        k += 1
        if k > n:
            result = False
            for index in indices:
                result = max(dfs(n - 1, index), result)
            if not result:
                break
            else:
                cycle = True
                break
        indices = set()
        distance_iter_prev = distance_iter
        for vertex in range(n):
            for neighbor_index, distance in adj_dict[vertex]:
                if distance_iter[vertex] < distance_iter[neighbor_index] + distance:
                    distance_iter[vertex] = distance_iter[neighbor_index] + distance
                    indices.add(vertex)
        if not indices:
            break

    if distance_iter[-1] != -math.inf:
        if not cycle:
            print(distance_iter[-1])
        else:
            print(':)')
    else:
        print(':(')


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    threading.stack_size(1000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
