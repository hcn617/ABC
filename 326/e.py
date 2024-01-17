MOD = 998244353

N = int(input())
A = [0] + list(map(int, input().split()))

p = pow(N, -1, MOD)  # 1/N

# dp[i]: iの目が出たときの、支給金額の期待値(過去にもらった分は含めない)
dp = [0] * (N + 1)
total = 0  # dp[i+1]以降の値の総和
for i in range(N, -1, -1):
    dp[i] = (total * p + A[i]) % MOD
    total = (total + dp[i]) % MOD

print(dp[0])
