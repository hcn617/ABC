class LazySegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def update(self, v, tl, tr, l, r):
        if l > r:
            return
        if l == tl and r == tr:
            self.lazy[v] ^= 1
        else:
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm))
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
        if self.lazy[v] % 2 == 1:
            self.tree[v] = (tr - tl + 1) - self.tree[v * 2] - self.tree[
                v * 2 + 1]
        else:
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]

    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        if self.lazy[v] % 2 == 1:
            self.tree[v] = (tr - tl + 1) - self.tree[v * 2] - self.tree[
                v * 2 + 1]
            self.lazy[v * 2] ^= 1
            self.lazy[v * 2 + 1] ^= 1
            self.lazy[v] = 0
        left = self.query(v * 2, tl, tm, l, min(r, tm))
        right = self.query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        return left + right


def process_queries(S, queries):
    N = len(S)
    A = [int(c) for c in S]
    seg_tree = LazySegmentTree(N)
    results = []

    for query in queries:
        c, L, R = query
        if c == 1:
            seg_tree.update(1, 0, N - 1, L - 1, R - 1)
        elif c == 2:
            max_length = seg_tree.query(1, 0, N - 1, L - 1, R - 1)
            results.append(max_length)

    return results


N,Q=map(int,input().split())
S=input()
queries = [list(map(int,input().split())) for _ in range(Q)]
results = process_queries(S, queries)
for ans in results:
    print(ans)
