import itertools
import random
def nextRand24(a, b):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield cur >> 8


def nextRand32(a, b):
    gen = nextRand24(a, b)
    while True:
        c = next(gen);
        d = next(gen)
        yield (c << 8) ^ d


def find_pivot(my_array):
    # Find good initial pivot
    list_of_lists = []
    n = len(my_array)
    for k in range(0, n, 5):
        list_of_lists.append(my_array[k:k + 5])
    for item in list_of_lists:
        item.sort()
    medians = [k[2] for k in list_of_lists[:-1]]
    medians.append(list_of_lists[-1][len(list_of_lists[-1]) // 2])
    # Found it
    initial_guess = sorted(medians)[(n // 5) // 2]

    del list_of_lists, medians
    return initial_guess


# Now the Pivot algo starts

def partition(array, left_index, right_index, q):
    pivot = random.choice(array[left_index: right_index + 1])
    i = left_index
    j = right_index
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] >= pivot and j >= 1:
            j -= 1
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    if q == i:
        print(pivot)
    elif q < i:
        partition(array, left_index, i - 1, q)
    else:
        partition(array, i, right_index, q)


n, stat = map(int, input().split())
a, b = map(int, input().split())
x = list(itertools.islice(nextRand32(a, b), n))  # данный массив
partition(x, 0, n - 1, stat - 1)
