from itertools import product

N, *P = map(int, input().split())
L = [int(input()) for _ in range(N)]

ans = 1 << 80
for pro in product(range(4), repeat=N):
    G = [[] for _ in range(4)]
    for l, pr in zip(L, pro):
        G[pr].append(l)

    is_ng = False
    for i in range(3):
        if len(G[i]) == 0:
            is_ng = True
            break
    if is_ng:
        continue

    now_ans = 0
    for i in range(3):
        now_ans += (len(G[i]) - 1) * 10
        now_ans += abs(sum(G[i]) - P[i])
    ans = min(ans, now_ans)

print(ans)
