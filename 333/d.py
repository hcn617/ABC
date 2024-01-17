import sys
import pypyjit

sys.setrecursionlimit(10 ** 7)
pypyjit.set_param('max_unroll_recursion=-1')


def size(v, par):
    result = 1
    for ch in G[v]:
        if ch == par:
            continue
        result += size(ch, v)
    return result


N = int(input())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)

P = []
for top in G[0]:
    P.append(size(top, 0))
ans = sum(P) - max(P) + 1
print(ans)
