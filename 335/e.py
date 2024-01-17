from atcoder.dsu import DSU

N, M = map(int, input().split())
A = list(map(int, input().split()))

G = [[] for _ in range(N)]
uf = DSU(N)
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)
    if A[u] == A[v]:
        uf.merge(u, v)

P = [(a, u) for u, a in enumerate(A)]  # (頂点に書かれた整数, 頂点の番号)
P.sort()
kind = [0] * N
kind[uf.leader(0)] = 1
for _a, u in P:
    for v in G[u]:
        u_leader, v_leader = uf.leader(u), uf.leader(v)
        if A[u] < A[v] or kind[v_leader] == 0:
            continue
        elif A[u] > A[v]:
            kind[u_leader] = max(kind[u_leader], kind[v_leader] + 1)

ans = kind[uf.leader(N - 1)]
print(ans)
