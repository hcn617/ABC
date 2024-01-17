from collections import deque

dic = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
si, sj, gi, gj = -1, -1, -1, -1
for i in range(H):
    for j in range(W):
        match A[i][j]:
            case a if a in dic:
                vi, vj = dic[a]
                ni, nj = i, j
                while True:
                    ni, nj = ni + vi, nj + vj
                    if not (0 <= ni < H and 0 <= nj < W):
                        break
                    if A[ni][nj] not in '.!':
                        break
                    A[ni][nj] = '!'
            case 'S':
                si, sj = i, j
            case 'G':
                gi, gj = i, j
                A[gi][gj] = '.'

que = deque()
que.append((si, sj))
dist = [[-1] * W for _ in range(H)]
dist[si][sj] = 0
while que:
    oi, oj = que.popleft()
    for ni, nj in [(oi, oj + 1), (oi, oj - 1), (oi + 1, oj), (oi - 1, oj)]:
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if A[ni][nj] != '.' or dist[ni][nj] != -1:
            continue
        dist[ni][nj] = dist[oi][oj] + 1
        que.append((ni, nj))
print(dist[gi][gj])
