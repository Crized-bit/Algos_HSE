import random
import sys


def generate():
    a = ''.join(random.choices(['a', 'b'], k=7))
    a = 'bbaabab'
    while True:
        if working(a) != testing(a):
            print(a)
            print(working(a))
            print(testing(a))
            sys.exit(0)


def working(a):
    def algo(pred, initial):
        final = pred + ['#'] + initial
        n = len(final)
        p = [0] * (n + 1)
        p[0] = -1
        for i in range(len(pred) + 2, n + 1):
            k = p[i - 1]
            while k != -1 and final[k] != final[i - 1]:
                k = p[k]
            p[i] = k + 1
            if (p[i] != p[i - 1] + 1 and p[i] != p[i - 1] - len(pred) + 1) or p[i] == 0:
                return False
        return True

    a = list(a)
    predict = []
    for j in range(0, len(a)):
        predict.append(a[j])
        if algo(predict, a[j + 1:]):
            return j + 1


def testing(a):
    n = len(a)
    z = [0] * n
    z[0] = n
    l = 0
    r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and a[z[i]] == a[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        if z[0] - z[i] == i:
            return i
    return n


generate()
