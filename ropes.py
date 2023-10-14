"""
Ropes. Dunno what algo to use...
"""

N, K = map(int, input().split())
input_length = []
for tmp in range(N):
    input_length.append(int(input()))


def bool_check(length) -> bool:
    if sum([k // length for k in input_length]) < K:
        return False
    else:
        return True


def bin_search(a, b) -> None:
    c = (a + b) // 2
    if b - a > 1:
        if bool_check(c):
            bin_search(c, b)
        else:
            bin_search(a, c)
    else:
        if bool_check(b):
            print(int(b))
        elif bool_check(a):
            print(int(a))
        else:
            print(0)


bin_search(1, sum(input_length))
