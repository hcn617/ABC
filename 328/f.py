class WeightedDSU:
    """重み付きUnionFind

    wuf=weighted_dsu(N): 初期化
    wuf.leader(x): xの根を返します。
    wuf.merge(x,y,w): weight(x)-weight(y)でx,yを結合
    wuf.same(x,y): xとyが同じグループに所属するかどうかを返す
    wuf.diff(x,y): weight(x)-weight(y)を返す
    """

    def __init__(self, n: int):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.weight = [0] * (n + 1)

    def leader(self, x: int) -> int:
        if self.par[x] == x:
            return x
        else:
            y = self.leader(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def merge(self, x: int, y: int, w: int):
        rx = self.leader(x)
        ry = self.leader(y)
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x: int, y: int) -> bool:
        return self.leader(x) == self.leader(y)

    def diff(self, x: int, y: int) -> bool:
        return self.weight[x] - self.weight[y]


N, Q = map(int, input().split())
uf = WeightedDSU(N)
ans_lst = []
for i in range(1, Q + 1):
    a, b, d = map(int, input().split())
    a, b = a - 1, b - 1
    if uf.same(a, b):
        if uf.diff(a, b) == d:
            ans_lst.append(i)
    else:
        uf.merge(a, b, d)
        ans_lst.append(i)

print(*ans_lst)
