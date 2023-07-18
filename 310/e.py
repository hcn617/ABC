def NAND(x, y):
    if x == y == 1:
        return 0
    return 1


N = int(input())
S = input()

dp = [[0] * 2 for _ in range(N + 1)]

for i, ss in enumerate(S):
    s = int(ss)
    dp[i + 1][NAND(s, 0)] += dp[i][0]
    dp[i + 1][NAND(s, 1)] += dp[i][1]
    dp[i + 1][s] += 1

ans = 0
for i in range(N + 1):
    ans += dp[i][1]
print(ans)
