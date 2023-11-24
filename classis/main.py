import typing

input = input().split()
output: list[int] = []
for value in input:
    if value == '+':
        output.append(output.pop() + output.pop())
        continue
    if value == '-':
        output.append(-output.pop() + output.pop())
        continue
    if value == '*':
        output.append(output.pop() * output.pop())
        continue
    output.append(int(value))
print(output[0])
