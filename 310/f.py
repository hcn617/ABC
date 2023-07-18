MOD = 998244353

N = int(input())
A = list(map(int, input().split()))

# dp[i][bit]: サイコロiまで見て、到達可能な数の状態bitに持っていける確率
dp = [[0] * (1 << 11) for _ in range(N + 1)]
dp[0][1] = 1


def next_bit(bit, num):
    ret = bit
    for i in range(11):
        if (bit >> i) & 1 and i + num <= 10:
            ret |= 1 << (i + num)
    return ret


for i, a in enumerate(A):
    p = pow(a, MOD - 2, MOD)  # p=1/a: サイコロiが特定の1つの目を出す確率
    for bit in range(1 << 11):
        for x in range(1, min(11, a + 1)):
            nbit = next_bit(bit, x)
            dp[i + 1][nbit] += dp[i][bit] * p % MOD
    if a > 10:
        q = p * (a - 10) % MOD  # サイコロiが11以上の目を出す確率()
        for bit in range(1 << 11):
            dp[i + 1][bit] += dp[i][bit] * q % MOD


ans = sum(dp[N][1 << 10:]) % MOD
print(ans)
