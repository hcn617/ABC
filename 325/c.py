from atcoder.dsu import DSU


def pos(i, j):
    return i * W + j


# 隣接する8頂点のリスト
def neighbor8(i, j):
    lst = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0: continue
            if 0 <= i + di < H and 0 <= j + dj < W:
                lst.append((i + di, j + dj))
    return lst


H, W = map(int, input().split())
S = [input() for _ in range(H)]

uf = DSU(H * W + 1)
dot = H * W  # ドット専用の頂点
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            uf.merge(pos(i, j), dot)
            continue
        # S[i][j]='#' のとき
        for i2, j2 in neighbor8(i, j):
            if S[i2][j2] == '#':
                uf.merge(pos(i, j), pos(i2, j2))

ans = len(uf.groups()) - 1
print(ans)
