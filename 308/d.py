from collections import deque


def is_next(e1, e2):
    T = "snuke"
    if e1 not in T or e2 not in T:
        return False
    i1 = T.index(e1)
    i2 = T.index(e2)
    if i2 == (i1 + 1) % 5:
        return True
    return False


H, W = map(int, input().split())
S = [input() for _ in range(H)]

que = deque()
que.append((0, 0))
seen = [[False] * W for _ in range(H)]
seen[0][0] = True

while que:
    oi, oj = que.popleft()
    oe = S[oi][oj]
    for ni, nj in [(oi + 1, oj), (oi - 1, oj), (oi, oj + 1), (oi, oj - 1)]:
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if seen[ni][nj]:
            continue
        ne = S[ni][nj]
        if is_next(oe, ne):
            seen[ni][nj] = True
            que.append((ni, nj))
if seen[-1][-1]:
    print("Yes")
else:
    print("No")
