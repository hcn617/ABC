S = input()
ans = []
for s in S:
    if s == '0':
        ans.append('0')
    elif s == '1':
        ans.append('1')
    elif s == 'B':
        if ans:
            ans.pop()

print(*ans, sep='')
