import math
from itertools import accumulate
from atcoder.segtree import SegTree


def dist(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)


N, K = map(int, input().split())
sx, sy = map(int, input().split())
house = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0.0] * N
P = []
for i in range(N - 1):
    x1, y1 = house[i]
    x2, y2 = house[i + 1]
    dx, dy = x2 - x1, y2 - y1
    P.append(math.sqrt(dx * dx + dy * dy))

acc = [0.0] + list(accumulate(P))
for i in range(N):
    acc[i] += dist(sx, sy, house[i][0], house[i][1])
dp = [0.0] * N
st = SegTree(min, 0, [0 for _ in range(N)])
dp[-1] = dist(house[-1][0], house[-1][1], sx, sy) * 2
st.set(N-1, dp[-1]+acc[-1])
for i in range(N-2, -1, -1):
    mi = st.prod(i+1, min(N, i+K+1))
    dp[i]=mi
