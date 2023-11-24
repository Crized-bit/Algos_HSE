import typing

N_dorms, N_letters = input().split()
N_flats_in_dorms_prefix: list[int] = []
N_flats_in_dorms: list[int] = []
for number in input().split():
    if N_flats_in_dorms_prefix:
        N_flats_in_dorms_prefix.append(int(number) + N_flats_in_dorms_prefix[-1])
    else:
        N_flats_in_dorms_prefix.append(int(number))
    N_flats_in_dorms.append(int(number))
adresses_for_letters = input().split()
prev_index = 0
for value in adresses_for_letters:
    while True:
        if (k:= N_flats_in_dorms_prefix[prev_index] - int(value)) >= 0:
            print(prev_index + 1, N_flats_in_dorms[prev_index] - k)
            break
        else:
            prev_index += 1
