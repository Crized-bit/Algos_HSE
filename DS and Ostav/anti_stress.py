import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    weights = [0 for i in range(n)]
    colors = [0 for j in range(n)]
    adj = {i: set() for i in range(n)}

    def dfs(vertex, adj_list, exp):
        weights[vertex] += exp
        colors[vertex] = 1
        for neighbor in adj_list[vertex]:
            if not colors[neighbor]:
                dfs(neighbor, adj_list, exp)

    for _ in range(m):
        user_command = sys.stdin.readline().rstrip().split()
        if user_command[0] == 'add':
            dfs(int(user_command[1]) - 1, adj, int(user_command[2]))
            colors = [0 for j in range(n)]
        elif user_command[0] == 'join':
            if int(user_command[1]) != int(user_command[2]):
                adj[int(user_command[1]) - 1].add(int(user_command[2]) - 1)
                adj[int(user_command[2]) - 1].add(int(user_command[1]) - 1)
        elif user_command[0] == 'get':
            print(weights[int(user_command[1]) - 1])


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    threading.stack_size(1000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
