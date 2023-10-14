"""
2 count sorts with duplicates!~
"""
from collections import Counter


def count_sort_with_duplicates(array: list[tuple], sort_index=0, revers=False) -> list[tuple]:
    max_number = 51
    duplicates = [[]] * max_number
    output = []
    for index, item_tuple in enumerate(array):
        if revers:
            if not duplicates[51 - item_tuple[sort_index]]:
                duplicates[51 - item_tuple[sort_index]] = [index]
            else:
                duplicates[51 - item_tuple[sort_index]].append(index)
        else:
            if not duplicates[item_tuple[sort_index]]:
                duplicates[item_tuple[sort_index]] = [index]
            else:
                duplicates[item_tuple[sort_index]].append(index)
    for i in range(max_number):
        index_of_elem = 0
        while index_of_elem != len(duplicates[i]):
            output.append(array[duplicates[i][index_of_elem]])
            index_of_elem += 1
    return output


# Read data
n, k = map(int, input().split())
N_tasks_and_times = []

for tmp in range(0, n):
    N_tasks_and_times.append(tuple(map(int, input().split())))
# Get dat sorts
N_tasks_and_times = count_sort_with_duplicates(N_tasks_and_times, 1)
N_tasks_and_times = count_sort_with_duplicates(N_tasks_and_times, 0, True)

# Get Place

print(Counter(N_tasks_and_times).get(N_tasks_and_times[k-1]))
