INF = 1 << 60

N = int(input())
takahashi, aoki = 0, 0
P = []
for _ in range(N):
    x, y, z = map(int, input().split())
    if x < y:
        mid = (x + y) // 2 + 1
        P.append((z * 2, mid - x))
        aoki += z
    else:
        takahashi += z
dist = aoki - takahashi
if dist < 0:
    print(0)
    exit()

# dp[i][j]: P[i]まで見て、aoki-tak=jの状態にするのに必要な最小コスト
dp = [[INF] * (dist + 1) for _ in range(len(P) + 1)]
dp[0][dist] = 0

for i in range(len(P)):
    z, cost = P[i]
    for j in range(dist + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        dp[i + 1][max(0, j - z)] = min(dp[i + 1][max(0, j - z)],
                                       dp[i][j] + cost)
ans = dp[-1][0]
print(ans)
