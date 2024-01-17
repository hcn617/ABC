from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b, x, y = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append((b, x, y))
    G[b].append((a, -x, -y))

que = deque()
que.append(0)
coord = [None] * N
coord[0] = [0, 0]
while que:
    v = que.popleft()
    ox, oy = coord[v]
    for nv, x, y in G[v]:
        if coord[nv] is not None:
            continue
        coord[nv] = [ox + x, oy + y]
        que.append(nv)

for i in range(N):
    if coord[i] is None:
        print("undecidable")
    else:
        print(*coord[i])
