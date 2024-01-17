from itertools import combinations
from math import lcm

MOD = 998244353

N, *A = map(int, input().split())

# P[i][j]: 2^i mod A[j]
P = [[1, 1, 1]]
for i in range(3):
    if A[i] == 1:
        P[0][i] = 0
for _ in range(60):
    T = P[-1][:]
    for i in range(3):
        T[i] = T[i] * 2 % A[i]
    P.append(T)

# dp[k][f1][f2][f3][m1][m2][m3]: cnt
# flag=0: なにしてもok, flag=1: やばい。
dp = [[[[[[[0 for _ in range(A[2])] for _ in range(A[1])] for _ in range(A[0])]
         for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in
      range(61)]

for k in range(59, -1, -1):
    if 1 << k > N:
        continue
    if 1 << (k + 1) > N:
        dp[k][0][0][0][0][0][0] = 1
        dp[k][1][1][0][P[k][0]][P[k][1]][0] = 1
        dp[k][1][0][1][P[k][0]][0][P[k][2]] = 1
        dp[k][0][1][1][0][P[k][1]][P[k][2]] = 1
        continue
    t = (N >> k) & 1
    for f1 in range(2):
        for f2 in range(2):
            for f3 in range(2):
                for m1 in range(A[0]):
                    for m2 in range(A[1]):
                        for m3 in range(A[2]):
                            for b1, b2, b3 in [(0, 0, 0), (1, 1, 0), (1, 0, 1),
                                               (0, 1, 1)]:
                                n1 = (m1 + b1 * P[k][0]) % A[0]
                                n2 = (m2 + b2 * P[k][1]) % A[1]
                                n3 = (m3 + b3 * P[k][2]) % A[2]
                                if (
                                        f1 == b1 == 1 or f2 == b2 == 1 or f3 == b3 == 1) and t == 0:
                                    continue
                                nf1, nf2, nf3 = f1, f2, f3
                                if b1 == 0 and t == 1:
                                    nf1 = 0
                                if b2 == 0 and t == 1:
                                    nf2 = 0
                                if b3 == 0 and t == 1:
                                    nf3 = 0
                                dp[k][nf1][nf2][nf3][n1][n2][n3] += dp[k + 1][
                                    f1][f2][f3][m1][m2][m3]
                                dp[k][nf1][nf2][nf3][n1][n2][n3] %= MOD

ans = 0
for f1 in range(2):
    for f2 in range(2):
        for f3 in range(2):
            ans += dp[0][f1][f2][f3][0][0][0]
ans %= MOD

for a1, a2 in combinations(A, 2):
    l = lcm(a1, a2)
    ans -= N // l
ans -= 1

ans %= MOD
print(ans)
