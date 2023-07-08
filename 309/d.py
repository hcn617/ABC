from collections import deque

N1, N2, M = map(int, input().split())

G1 = [[] for _ in range(N1)]
G2 = [[] for _ in range(N1 + N2)]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if a >= N1:
        G2[a].append(b)
        G2[b].append(a)
    else:
        G1[a].append(b)
        G1[b].append(a)


def bfs(s, G):
    que = deque()
    que.append(s)
    dist = [-1] * len(G)
    dist[s] = 0
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                que.append(nv)
    return max(dist)


print(bfs(0, G1) + bfs(N1 + N2 - 1, G2) + 1)
