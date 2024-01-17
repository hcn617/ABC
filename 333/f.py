import sys
import pypyjit

sys.setrecursionlimit(10 ** 7)
pypyjit.set_param('max_unroll_recursion=-1')

MOD = 998244353
INV = (MOD + 1) // 2  # 1/2 mod 998244353


def solve(x):
    if x == 1:
        return [1]

    prev = solve(x - 1)
    a0 = 0
    for i in range(x - 1):
        a0 += prev[x - i - 2] * inv[i + 2] % MOD
        a0 %= MOD
    a0 = a0 * rui[x] % MOD * pow(rui[x] - 1, MOD - 2, MOD) % MOD
    result = [a0]
    for i in range(1, x):
        result.append((prev[i - 1] + result[-1]) * inv[1] % MOD)
    return result


N = int(input())

rui = [1]  # rui[x]: 2^x mod 998244353
inv = [1]  # inv[x]: (1/2)^x mod 998244353
for i in range(N + 2):
    rui.append(rui[-1] * 2 % MOD)
    inv.append(inv[-1] * INV % MOD)

print(*solve(N))
