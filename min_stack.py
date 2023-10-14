import heapq

imp_len = int(input())
push_stack = []
pop_stack = []

for tmp in range(imp_len):
    value = input()
    if value[0] == '+':
        if len(push_stack) == 0:
            push_stack.append((int(value[1:]), int(value[1:])))
        else:
            push_stack.append((int(value[1:]), min(push_stack[-1][1], int(value[1:]))))
    elif value[0] == '-':
        if len(pop_stack) == 0:
            item_of_push = push_stack.pop()[0]
            pop_stack.append((item_of_push, item_of_push))
            for k in range(len(push_stack)):
                item_of_push = push_stack.pop()[0]
                pop_stack.append((item_of_push, min(item_of_push, pop_stack[-1][1])))
        pop_stack.pop()
        if len(push_stack) + len(pop_stack) == 0:
            print(-1)
            continue
    if push_stack and pop_stack:
        print(min(push_stack[-1][1], pop_stack[-1][1]))
    elif push_stack:
        print(push_stack[-1][1])
    else:
        print(pop_stack[-1][1])
