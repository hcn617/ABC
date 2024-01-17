from collections import deque

INF = 1 << 60

N, M = map(int, input().split())
G = [[] for _ in range(N)]
dic = dict()
for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append((b, c))
    G[b].append((a, c))
    dic[(a, b)] = c
    dic[(b, a)] = c

dp = [[-INF] * N for _ in range(1 << N)]
que = deque()
for i in range(N):
    dp[1 << i][i] = 0
    que.append((1 << i, i))

ans = -1
while que:
    state, ov = que.popleft()
    ans = max(ans, dp[state][ov])
    for nv in range(N):
        nex_state = state | (1 << nv)
        if nex_state == state:
            continue
        if (ov, nv) not in dic:
            continue
        nex_cost = dp[state][ov] + dic[(ov, nv)]
        if dp[nex_state][nv] == -INF:
            dp[nex_state][nv] = nex_cost
            que.append((nex_state, nv))
        elif dp[nex_state][nv] < nex_cost:
            dp[nex_state][nv] = nex_cost

print(ans)
