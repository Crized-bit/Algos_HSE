import sys

n = int(sys.stdin.readline())

numbers: list[int] = [0] * (n + 1)
for k in range(2, n + 1):
    if k == 1:
        pass
    output = numbers[k - 1]
    if not k % 2:
        output = min(numbers[k // 2], output)
    if not k % 3:
        output = min(numbers[k // 3], output)
    if numbers[k] != 0:
        numbers[k] = min(numbers[k], output + 1)
    else:
        numbers[k] = output + 1
print(numbers[-1])
tmp = len(numbers) - 1
final_array = [tmp]
tmp_1 = tmp
while tmp > 1:
    if numbers[tmp] - numbers[tmp - 1] == 1:
        tmp_1 -= 1
    if not tmp % 2:
        if numbers[tmp] - numbers[tmp // 2] == 1:
            tmp_1 = min(tmp, tmp // 2)
    if not tmp % 3:
        if numbers[tmp] - numbers[tmp // 3] == 1:
            tmp_1 = min(tmp, tmp // 3)
    final_array.append(tmp_1)
    tmp = tmp_1
print(*reversed(final_array))