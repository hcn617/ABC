from collections import deque

vec = [(-1, 0), (0, -1), (-1, -1)]

H, W, N = map(int, input().split())
Grid = [[-1] * W for _ in range(H)]
que = deque()
for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    que.append((a, b))
    Grid[a][b] = 0


# 左上が点(i, j) になる正方形の、1辺の長さの最大値
def f(i, j):
    return min(H - i, W - j)


while que:
    oi, oj = que.popleft()
    for vi, vj in vec:
        ni, nj = oi + vi, oj + vj
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if Grid[ni][nj] != -1:
            continue
        Grid[ni][nj] = Grid[oi][oj] + 1
        que.append((ni, nj))

ans = 0
for i in range(H):
    for j in range(W):
        if Grid[i][j] == -1:
            ans += f(i, j)
            continue
        ans += min(Grid[i][j], f(i, j))
print(ans)
