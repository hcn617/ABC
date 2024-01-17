S = input()

ans_stack = ["X", "X"]
for s in S:
    ans_stack.append(s)
    if ''.join(ans_stack[-3:]) == "ABC":
        for _ in range(3):
            ans_stack.pop()

print(*ans_stack[2:], sep="")
