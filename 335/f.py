MOD = 998244353
SQ = 100  # 大小の境界(100くらいがいいかなと思います)

N = int(input())
A = list(map(int, input().split()))

black, white = [0] * N, [0] * N
black[0] = 1
dp = [[0] * (SQ + 1) for _ in range(N)]
for i in range(N - 1):
    if A[i] <= SQ:
        dp[i][A[i]] += black[i]
    else:
        for next_i in range(i + A[i], N, A[i]):
            black[next_i] += black[i]
            black[next_i] %= MOD
    for v in range(1, SQ + 1):
        next_i = i + v
        if next_i >= N:
            break
        dp[next_i][v] = dp[i][v]
        black[next_i] += dp[i][v]
        black[next_i] %= MOD
    white[i + 1] = (black[i] + white[i]) % MOD

ans = (black[-1] + white[-1]) % MOD
print(ans)
