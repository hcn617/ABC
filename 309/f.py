from operator import itemgetter

'''
syakayamiさん作、PythonバージョンのACLよりコピペしたものです。
使わせていただきありがとうございます！
https://github.com/shakayami/ACL-for-python/blob/master/segtree.py

・使い方(個人的なまとめ)
sg=segtree((初期値リストA), (演算func), (単位元ide_ele))
A: 初期値リスト。問題で与えられてるのをそのまま入れることが多い。
func, ide_ele: 演算とそれに対応する単位元。
　例）add,0 (足し算、単位元0)
詳しいことは下のURLに書いてます。
https://github.com/shakayami/ACL-for-python/wiki/segtree
'''


class segtree():
    n = 1
    size = 1
    log = 2
    d = [0]
    op = None
    e = 10 ** 15

    def __init__(self, V, OP, E):
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [E for i in range(2 * self.size)]
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        assert 0 <= p and p < self.n
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        assert 0 <= p and p < self.n
        return self.d[p + self.size]

    def prod(self, l, r):
        assert 0 <= l and l <= r and r <= self.n
        sml = self.e
        smr = self.e
        l += self.size
        r += self.size
        while (l < r):
            if (l & 1):
                sml = self.op(sml, self.d[l])
                l += 1
            if (r & 1):
                smr = self.op(self.d[r - 1], smr)
                r -= 1
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def max_right(self, l, f):
        assert 0 <= l and l <= self.n
        assert f(self.e)
        if l == self.n:
            return self.n
        l += self.size
        sm = self.e
        while (1):
            while (l % 2 == 0):
                l >>= 1
            if not (f(self.op(sm, self.d[l]))):
                while (l < self.size):
                    l = 2 * l
                    if f(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, f):
        assert 0 <= r and r < self.n
        assert f(self.e)
        if r == 0:
            return 0
        r += self.size
        sm = self.e
        while (1):
            r -= 1
            while (r > 1 & (r % 2)):
                r >>= 1
            if not (f(self.op(self.d[r], sm))):
                while (r < self.size):
                    r = (2 * r + 1)
                    if f(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r:
                break
        return 0

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


N = int(input())
Box = []
Vs = [[] for _ in range(3)]
for _ in range(N):
    bi = list(map(int, input().split()))
    bi.sort()
    for i in range(3):
        Vs[i].append(bi[i])
    Box.append(bi)

# 座圧する
for i in range(3):
    Vs[i].sort()
dic = [dict() for _ in range(3)]
for i in range(3):
    for el in Vs[i]:
        if el not in dic[i]:
            v = len(dic[i])
            dic[i][el] = v
for i in range(N):
    for j in range(3):
        Box[i][j] = dic[j][Box[i][j]]
# print(Box)

# box[0]の小さい順に箱を見てく
Box.sort(key=lambda x: (x[0], -x[1]))
st = segtree([1 << 60] * (N + 1), min, 1 << 60)
for a, b, c in Box:
    if st.prod(0, b) < c:
        print("Yes")
        exit()
    if st.prod(b, b + 1) > c:
        st.set(b, c)
print("No")
