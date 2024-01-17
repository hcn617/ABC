from atcoder.dsu import DSU

MOD = 998244353


def pos(i, j):
    return i * W + j


H, W = map(int, input().split())
S = [input() for _ in range(H)]

red = []
uf = DSU(H * W)
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            for ni, nj in [(i + 1, j), (i, j + 1)]:
                if not (0 <= ni < H and 0 <= nj < W):
                    continue
                if S[ni][nj] == '#':
                    uf.merge(pos(i, j), pos(ni, nj))
        else:
            red.append((i, j))

prev_cnt = len(uf.groups()) - len(red)

ans = 0
for i, j in red:
    se = set()
    for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if S[ni][nj] == '#':
            se.add(uf.leader(pos(ni, nj)))
    ans += prev_cnt - len(se) + 1
    ans %= MOD
ans = ans * pow(len(red), MOD - 2, MOD) % MOD
print(ans)
