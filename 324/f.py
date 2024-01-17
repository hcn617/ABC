R = 10 ** 9

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, b, c = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append((v, b * R, c))


def judge(m):
    dp = [-float("Inf") for _ in range(N)]
    dp[0] = 0
    for i in range(N - 1):
        for j, b, c in G[i]:
            dp[j] = max(dp[j], dp[i] + b - c * m)
    return dp[-1] >= 0


ok, ng = 0, 10_001 * R
while ng - ok > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid

print(ok / R)
