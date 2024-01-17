INF = 1 << 40

N = int(input())
checkpoint = [tuple(map(int, input().split())) for _ in range(N)]


# チェックポイントi,j間の距離
def dist(i, j):
    xi, yi = checkpoint[i]
    xj, yj = checkpoint[j]
    dx = xi - xj
    dy = yi - yj
    return (dx * dx + dy * dy) ** 0.5


# penalty[i]: チェックポイントをi回スルーしたときのペナルティ
penalty = [0, 1]
for _ in range(32):
    penalty.append(penalty[-1] << 1)

# dp[i][j]: 最終地点i、スルーした回数jの最短距離
dp = [[INF] * 32 for _ in range(N)]
dp[0][0] = 0

for i in range(1, N):
    for j in range(32):
        d = i - 1 - j
        for i2 in range(i - 1, -1, -1):
            j2 = i2 - d
            if j2 < 0:
                break
            dp[i][j] = min(dp[i][j], dp[i2][j2] + dist(i, i2))

ans = INF
for j in range(31):
    ans = min(ans, dp[N - 1][j] + penalty[j])
print(ans)
