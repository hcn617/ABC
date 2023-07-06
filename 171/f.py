MOD = 10 ** 9 + 7


class nCr:
    def __init__(self, n_max, mod):
        self.rui = [1] * (n_max + 1)
        for i in range(2, n_max + 1):
            self.rui[i] = self.rui[i - 1] * i % mod
        self.mod = mod

    def value(self, n, r):
        bunshi = self.rui[n]
        bunbo = self.rui[n - r] * self.rui[r] % self.mod
        val = bunshi * pow(bunbo, self.mod - 2, self.mod) % self.mod
        return val


K = int(input())
S = input()

rui25 = [1]
rui26 = [1]
for i in range(K):
    rui25.append(rui25[-1] * 25 % MOD)
    rui26.append(rui26[-1] * 26 % MOD)

ncr = nCr(K - 1 + len(S), MOD)

ans = 0
for i in range(K + 1):
    ans += rui25[i] * rui26[K - i] % MOD * ncr.value(i + len(S) - 1,
                                                     len(S) - 1) % MOD
    ans %= MOD
print(ans)
