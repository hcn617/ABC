class dsu():
    """Union-Find

    syakayamiさん作、PythonバージョンのACLよりコピペしたものです。
    使わせていただきありがとうございます！
    https://github.com/shakayami/ACL-for-python/blob/master/dsu.py

    ・使い方(個人的まとめ):
        uf=dsu(N): 初期化(Nは頂点の数)
        uf.merge(a,b): 頂点aがある連結成分と頂点bがある連結成分を合体します。
        uf.same(a,b): 頂点a,bが同じ連結成分ならTrue, そうでないならFalseを返します。
        uf.leader(a): 頂点aの連結成分の代表元を返します。
        uf.size(a): 頂点aの連結成分にある超点数を返します(頂点a自身を含みます)。
        uf.groups(): グラフの連結成分の情報を答えます。

    ・使い方URL
        https://github.com/shakayami/ACL-for-python/wiki/dsu
    """
    n = 1
    parent_or_size = [-1 for i in range(n)]

    def __init__(self, N):
        self.n = N
        self.parent_or_size = [-1 for i in range(N)]

    def merge(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if (-self.parent_or_size[x] < -self.parent_or_size[y]):
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        if (self.parent_or_size[a] < 0):
            return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [0 for i in range(self.n)]
        group_size = [0 for i in range(self.n)]
        for i in range(self.n):
            leader_buf[i] = self.leader(i)
            group_size[leader_buf[i]] += 1
        result = [[] for i in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)
        result2 = []
        for i in range(self.n):
            if len(result[i]) > 0:
                result2.append(result[i])
        return result2


N = int(input())
si, sj, ti, tj = map(int, input().split())
circle = []
for _ in range(N):
    x, y, r = map(int, input().split())
    circle.append((x, y, r))


def is_ok(i, j):
    x1, y1, r1 = circle[i]
    x2, y2, r2 = circle[j]
    dx, dy = x2 - x1, y2 - y1
    d2 = dx * dx + dy * dy
    return (r1 - r2) ** 2 <= d2 <= (r1 + r2) ** 2


uf = dsu(N + 2)
for i in range(N - 1):
    for j in range(i + 1, N):
        if is_ok(i, j):
            uf.merge(i, j)

for ci in range(N):
    i, j, r = circle[ci]
    ds2 = (si - i) ** 2 + (sj - j) ** 2
    if ds2 == r * r:
        uf.merge(ci, N)
    dt2 = (ti - i) ** 2 + (tj - j) ** 2
    if dt2 == r * r:
        uf.merge(ci, N + 1)

if uf.same(N, N + 1):
    print("Yes")
else:
    print("No")
