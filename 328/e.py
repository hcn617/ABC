from itertools import combinations
from atcoder.dsu import DSU

N, M, K = map(int, input().split())
edge = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edge.append((u - 1, v - 1, w))

ans = 1 << 70
for comb in combinations(range(M), N - 1):
    uf = DSU(N)
    total_cost = 0
    for i in comb:
        u, v, w = edge[i]
        uf.merge(u, v)
        total_cost += w
    if len(uf.groups()) == 1:
        ans = min(ans, total_cost % K)

print(ans)
