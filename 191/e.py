from heapq import heappop, heappush

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append((b - 1, c))

for i in range(N):
    que = []
    heappush(que, (0, i))
    dist = [-1] * N
    while que:
        cost, v = heappop(que)
        if cost > dist[v] and (cost, v) != (0, i):
            continue
        for nv, pc in G[v]:
            nc = cost + pc
            if dist[nv] == -1 or nc < dist[nv]:
                dist[nv] = nc
                heappush(que, (nc, nv))
    print(dist[i])
