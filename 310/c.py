N = int(input())

se = set()
for _ in range(N):
    S = input()
    T = reversed(S)
    if S in se or T in se:
        continue
    else:
        se.add(S)
print(len(se))
