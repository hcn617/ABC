from collections import deque

N, M = map(int, input().split())
S = [input() for _ in range(N)]

T = [[False] * M for _ in range(N)]
T[1][1] = True

seen = set()
vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]
que = deque()
que.append((1, 1))
seen.add((1, 1))

while que:
    oi, oj = que.popleft()
    for vi, vj in vec:
        for k in range(1, 1000):
            ni, nj = oi + vi * k, oj + vj * k
            if S[ni][nj] == '.':
                T[ni][nj] = True
            else:
                ni -= vi
                nj -= vj
                if (ni, nj) not in seen:
                    seen.add((ni, nj))
                    que.append((ni, nj))
                break

ans = 0
for i in range(N):
    for j in range(M):
        if T[i][j]:
            ans += 1
print(ans)
