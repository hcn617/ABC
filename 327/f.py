from atcoder.lazysegtree import LazySegTree

T_MAX = 200_003
X_MAX = 200_003

#  TODO (区間演算opの単位元 op(ele1, e) = ele1)
e = 0


# 区間演算
def op(ele1, ele2):
    return max(ele1, ele2)


def mapping(func, ele):
    return func + ele


def composition(func_upper, func_lower):
    return func_upper + func_lower


# mapping(func, ele) = ele となるようなfunc
id_ = 0

# TODO (初期リストv)
lazy_segtree = LazySegTree(op, e, mapping, composition, id_, [0] * T_MAX)

N, D, W = map(int, input().split())
G = [[] for _ in range(T_MAX)]
for _ in range(N):
    t, x = map(int, input().split())
    G[t].append(x)

for i in range(D):
    for x in G[i]:
        left = max(0, x - W + 1)
        lazy_segtree.apply(left, x + 1, 1)

ans = 0
for i in range(1, T_MAX):
    for x in G[i - 1]:
        left = max(0, x - W + 1)
        lazy_segtree.apply(left, x + 1, -1)
    if i + D - 1 < T_MAX:
        for x in G[i + D - 1]:
            left = max(0, x - W + 1)
            lazy_segtree.apply(left, x + 1, 1)
    ans = max(ans, lazy_segtree.all_prod())

print(ans)
