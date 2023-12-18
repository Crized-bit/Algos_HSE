import sys
import threading
from concurrent.futures import ThreadPoolExecutor


class DCU:
    def __init__(self, element_count):
        self.parent = [i for i in range(element_count)]
        self.rang = [0] * element_count
        self.weight = [0] * element_count

    def add(self, x, exp):
        self.weight[self.find(x, [])] += exp

    def find(self, x, array):
        if self.parent[x] != x:
            for i in range(len(array)):
                array[i] += self.weight[x]
            array.append(self.weight[x])
            parent = self.find(self.parent[x], array)
            self.parent[x] = parent
            self.weight[x] = array.pop()
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x, [])
        y = self.find(y, [])

        if x == y:
            return
        if self.rang[x] > self.rang[y]:
            x, y = y, x

        self.parent[x] = y

        self.weight[x] -= self.weight[y]
        if self.rang[x] == self.rang[y]:
            self.rang[y] += 1


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    my_dsu = DCU(n)

    for _ in range(m):
        user_command = sys.stdin.readline().rstrip().split()
        if user_command[0] == 'add':
            my_dsu.add(int(user_command[1]) - 1, int(user_command[2]))
        elif user_command[0] == 'join':
            my_dsu.union(int(user_command[1]) - 1, int(user_command[2]) - 1)
        elif user_command[0] == 'get':
            if int(user_command[1]) - 1 == my_dsu.parent[int(user_command[1]) - 1]:
                print(my_dsu.weight[int(user_command[1]) - 1])
            else:
                print(my_dsu.weight[my_dsu.find(int(user_command[1]) - 1, [])] + my_dsu.weight[int(user_command[1]) - 1])


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    threading.stack_size(1000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
