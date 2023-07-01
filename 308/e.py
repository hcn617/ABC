N = int(input())
A = list(map(int, input().split()))
S = input()


def mex_bit(bit):
    if bit & 1 == 0:
        return 0
    if bit & (1 << 1) == 0:
        return 1
    if bit & (1 << 2) == 0:
        return 2
    return 3


dp = [[0] * 8 for _ in range(3)]
for a, s in zip(A, S):
    if s == 'M':
        dp[0][1 << a] += 1
    elif s == 'E':
        for j in range(8):
            nj = j | (1 << a)
            dp[1][nj] += dp[0][j]
    elif s == 'X':
        for j in range(8):
            nj = j | (1 << a)
            dp[2][nj] += dp[1][j]

ans = 0
for bit in range(8):
    ans += mex_bit(bit) * dp[2][bit]
print(ans)
