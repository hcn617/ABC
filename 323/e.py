MOD = 998244353

N, X = map(int, input().split())
T = list(map(int, input().split()))

inv = pow(N, MOD - 2, MOD)

# dp[i][t]: 曲iが時刻t+0.5に流れている確率(imos)
dp = [[0] * (X + 1) for _ in range(N)]
ep = [0] * (X + 1)  # ep[t]: 時刻tに新たに曲をかけ始める確率
ep[0] = 1

for t in range(X + 1):
    p = ep[t]  # 新たに曲をかけ始める確率
    q = p * inv % MOD  # q = p/N 特定の曲をかけ始める確率
    for i in range(N):
        dp[i][t] += q
        dp[i][t] %= MOD
        nt = t + T[i]
        if nt <= X:
            ep[nt] += q
            ep[nt] %= MOD
            dp[i][nt] -= q
            dp[i][nt] %= MOD
lst = dp[0][:]
for i in range(X):
    lst[i + 1] += lst[i]
    lst[i + 1] %= MOD

print(lst[X])
