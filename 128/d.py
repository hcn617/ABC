N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = -1
for left_cnt in range(N + 1):
    for right_cnt in range(N + 1 - left_cnt):
        pop_cnt = K - left_cnt - right_cnt
        if pop_cnt < 0:
            break
        P = V[:left_cnt] + V[N - right_cnt:]
        P.sort(reverse=True)
        for _ in range(pop_cnt):
            if P and P[-1] < 0:
                P.pop()
        ans = max(ans, sum(P))

print(ans)
