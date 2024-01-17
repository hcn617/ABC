def lst2int(lst):
    val = 0
    for i, el in enumerate(lst):
        val += el * ((P + 1) ** i)
    return val


def int2lst(v):
    ret = []
    val = v
    for _ in range(K):
        val, mo = divmod(val, P + 1)
        ret.append(mo)
    return ret


N, K, P = map(int, input().split())

dp = [1 << 40] * ((P + 1) ** K)
dp[0] = 0

for _ in range(N):
    c, *A = map(int, input().split())
    nex = dp[:]
    for i, cost in enumerate(dp):
        lst = int2lst(i)
        nex_lst = [min(el1 + el2, P) for el1, el2 in zip(A, lst)]
        nex_int = lst2int(nex_lst)
        nex[nex_int] = min(nex[nex_int], cost + c)
    dp = nex

if dp[-1] >= 1 << 40:
    dp[-1] = -1
print(dp[-1])
