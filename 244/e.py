MOD = 998244353

N, M, K, S, T, X = map(int, input().split())
X -= 1
S -= 1
T -= 1
# X と N+X の間は強制移動レーン
G = [[] for _ in range(N * 2)]  # [表世界]+[裏世界]
for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    if v == X:
        G[u].append(v + N)
        G[u + N].append(v)
    else:
        G[u].append(v)
        G[u + N].append(v + N)

    if u == X:
        G[v].append(u + N)
        G[v + N].append(u)
    else:
        G[v].append(u)
        G[v + N].append(u + N)

Count = [[0] * (N * 2) for _ in range(K + 1)]
Count[0][S] = 1

for t in range(K):
    for pv in range(N * 2):
        for nex in G[pv]:
            Count[t + 1][nex] += Count[t][pv]
            if Count[t + 1][nex] >= MOD:
                Count[t + 1][nex] -= MOD
print(Count[K][T])
