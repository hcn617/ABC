import sys

"""再帰関数のときセット
sys.setrecursionlimit(10**7)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
"""
N, T, M = map(int, input().split())

C = set()
for _ in range(M):
    a, b = map(int, input().split())
    C.add((a - 1, b - 1))
    C.add((b - 1, a - 1))

ans = 0


def f(v, lis):
    if v == N:
        if len(lis[-1]) == 0:
            return
        global ans
        ans += 1
        return

    for i in range(T):
        nlis = [a[:] for a in lis]
        if len(nlis[i]) == 0:
            nlis[i].append(v)
            f(v + 1, nlis)
            break

        is_ok = True
        for v2 in nlis[i]:
            if (v, v2) in C:
                is_ok = False
        if is_ok:
            nlis[i].append(v)
            f(v + 1, nlis)


f(0, [[] for _ in range(T)])

print(ans)
