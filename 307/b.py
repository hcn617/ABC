N = int(input())
S = [input() for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        T = S[i] + S[j]
        if T == reversed(T):
            ans += 1

print(ans)