import sys

rows, cols, n_builds = map(int, sys.stdin.readline().rstrip().split())
colors = [0] * (rows * cols)
game_map = {i: set() for i in range(rows * cols)}
for i in range(rows):
    for j in range(cols):
        if i != rows - 1:
            game_map[i * cols + j].add((i + 1) * cols + j)
        if j != cols - 1:
            game_map[i * cols + j].add(i * cols + j + 1)


def dfs(vertex, adj, bans, color):
    color[vertex] = 1
    if vertex == rows * cols - 1:
        return True
    for neighbor in adj[vertex] - bans:
        if not color[neighbor]:
            result = dfs(neighbor, adj, bans, color)
            if result:
                return True
    return False


buildings = []
for i in range(n_builds):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    x -= 1
    y -= 1

    buildings.append(x * cols + y)

ban = set(buildings)
if dfs(0, game_map, ban, colors):
    print(-1)
    sys.exit(0)
else:
    left, right = 0, n_builds
    while (right - left) > 1:
        colors = [0] * (rows * cols)
        mid = (left + right) // 2
        ban = set(buildings[0: mid])
        if dfs(0, game_map, ban, colors):
            left = mid
        else:
            right = mid
    print(left + 1)
