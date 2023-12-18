import random
import sys
import threading
from concurrent.futures import ThreadPoolExecutor


def generate():
    while True:
        n, m = random.randint(100, 1000), random.randint(30, 50)
        input_list = []
        for i in range(m):
            command = random.randint(1, 3)
            if command == 1:
                input_list.append(f'get {random.randint(1, n)}')
            elif command == 2:
                input_list.append(f'join {random.randint(1, n)} {random.randint(1, n)}')
            else:
                input_list.append(f'add {random.randint(1, n)} {random.randint(1, 100)}')

        if (p := main_pasha(n, input_list)) != (p2 := main_pasha_2(n, input_list)) != (d := main_danil(n, input_list)):
            print(n, m)
            print(*input_list, sep='\n')
            print(p, p2, d)
            break


def main_pasha(n, commands):
    weights = [0 for i in range(n)]
    colors = [0 for j in range(n)]
    adj = {i: set() for i in range(n)}

    def dfs(vertex, adj_list, exp):
        weights[vertex] += exp
        colors[vertex] = 1
        for neighbor in adj_list[vertex]:
            if not colors[neighbor]:
                dfs(neighbor, adj_list, exp)

    result_list = []
    for command in commands:
        user_command = command.split()
        if user_command[0] == 'add':
            dfs(int(user_command[1]) - 1, adj, int(user_command[2]))
            colors = [0 for j in range(n)]
        elif user_command[0] == 'join':
            if int(user_command[1]) != int(user_command[2]):
                adj[int(user_command[1]) - 1].add(int(user_command[2]) - 1)
                adj[int(user_command[2]) - 1].add(int(user_command[1]) - 1)
        else:
            result_list.append(weights[int(user_command[1]) - 1])

    return result_list


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


def main_pasha_2(n, commands):
    my_dsu = DCU(n)
    result_list = []
    for command in commands:
        user_command = command.split()
        if user_command[0] == 'add':
            my_dsu.add(int(user_command[1]) - 1, int(user_command[2]))
        elif user_command[0] == 'join':
            if my_dsu.parent[int(user_command[1]) - 1] != my_dsu.parent[int(user_command[2]) - 1]:
                my_dsu.union(int(user_command[1]) - 1, int(user_command[2]) - 1)
        elif user_command[0] == 'get':
            if int(user_command[1]) - 1 == my_dsu.parent[int(user_command[1]) - 1]:
                result_list.append(my_dsu.weight[int(user_command[1]) - 1])
            else:
                result_list.append(
                    my_dsu.weight[my_dsu.find(int(user_command[1]) - 1, [])] + my_dsu.weight[int(user_command[1]) - 1])
    return result_list


class DisjointSet:
    def __init__(self, users):
        self.parents = users
        self.rank = [0] * len(users)
        self.score = [0] * len(users)

    def join(self, user1, user2):
        par_us1 = self.get(user1)[0]
        par_us2 = self.get(user2)[0]
        if par_us1 == par_us2:
            return
        if self.rank[par_us1] < self.rank[par_us2]:
            par_us1, par_us2 = par_us2, par_us1
        elif self.rank[par_us2] == self.rank[par_us1]:
            self.rank[user1] += 1
        self.parents[par_us2] = par_us1
        self.score[par_us2] -= self.score[par_us1]

    def add(self, user, award):
        self.score[self.get(user)[0]] += award

    def get(self, user):
        if self.parents[user] == user:
            return user, 0
        get_ = self.get(self.parents[user])
        self.score[user] += get_[1]
        self.parents[user] = get_[0]
        return self.parents[user], self.score[user]


def main_danil(n, commands):
    dsu = DisjointSet([i for i in range(n)])
    for command in commands:
        req = command.split()
        if req[0] == 'add':
            dsu.add(int(req[1]) - 1, int(req[2]))
        elif req[0] == 'get':
            user = int(req[1])
            par = dsu.get(user - 1)[0]
            print(dsu.score[user - 1] + (0 if par == user - 1 else dsu.score[par]))
        else:
            us1 = int(req[1]) - 1
            us2 = int(req[2]) - 1
            dsu.join(us1, us2)


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    threading.stack_size(1000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(generate)
        future.result()
