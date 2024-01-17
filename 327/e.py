import math

INF = float("Inf")

N = int(input())
P = list(map(int, input().split()))

# rui[i]: (0.9)^i
rui = [1]
for _ in range(N):
    rui.append(rui[-1] * 0.9)
# bunbo[j]: 参加回数jのときの、第1項分母
bunbo = [0]
for i in range(N):
    bunbo.append(bunbo[-1] + rui[i])
# penalty[j]: 参加回数jのときの、第2項
penalty = [INF]
for i in range(N):
    penalty.append(1200 / math.sqrt(i + 1))

# dp[i][j]: (後ろから順に)P[i]まで見て、参加した回数jのときの第1項分子の最大値
dp = [[-INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = 0

for i in range(N - 1, -1, -1):
    for j in range(1, N - i + 1):
        # 参加しないパターン。そのままコピーしてくる
        dp[i][j] = dp[i + 1][j]
        # 参加するパターン
        v = dp[i + 1][j - 1] + rui[j - 1] * P[i]
        dp[i][j] = max(dp[i][j], v)

ans = -INF
for i in range(N):
    for j in range(1, N - i + 1):
        ans = max(ans, dp[i][j] / bunbo[j] - penalty[j])

print(ans)
