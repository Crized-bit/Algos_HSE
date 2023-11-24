"""
My algo sounds like O(N^3) :(
"""
import sys

n, L = map(int, sys.stdin.readline().rstrip().split())
array = []
for i in range(n):
    # Кстати, решение с numpy намного легче работает со строками, я его пушил - меня забанили
    array.append([*map(int, sys.stdin.readline().rstrip().split())])
for i in range(n):
    for k in range(n - L + 1):
        array[i][k] = min(array[i][k:k + L])
for i in range(n - L + 1):
    for k in range(n - L + 1):
        array[i][k] = min([array[z][k] for z in range(i, i + L)])
for i in range(n - L + 1):
    print(*array[i][:n - L + 1])
