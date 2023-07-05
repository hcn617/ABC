class fenwick_tree():
    """Fenwick Tree

    Fenwick Treeです。
    数列A[i]に対して、以下の2つのクエリを高速に行います。
    ・A[i]の値を更新する。
    ・A[0]~A[k-1]の総和を求める

    使い方(個人的まとめ):
        ft=fenwick_tree(N) #[0]*Nをつくる。
        ft.add(p,x): p番目(0-index)の値にxをプラスする。
        ft.sum(l,r): l番目からr-1番目までの和を求める。(これも0-index)

    使い方wikiのURL:
        https://github.com/shakayami/ACL-for-python/wiki/fenwicktree

    コピー元のURL:
        https://github.com/shakayami/ACL-for-python/blob/master/fenwicktree.py

    Attributes:
        N (int): 数列の長さ

    """

    n = 1
    data = [0 for i in range(n)]

    def __init__(self, N):
        self.n = N
        self.data = [0 for i in range(N)]

    def add(self, p, x):
        assert 0 <= p < self.n, "0<=p<n,p={0},n={1}".format(p, self.n)
        p += 1
        while (p <= self.n):
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        assert (
                0 <= l and l <= r and r <= self.n), "0<=l<=r<=n,l={0},r={1},n={2}".format(
            l, r, self.n)
        return self.sum0(r) - self.sum0(l)

    def sum0(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            r -= r & -r
        return s


N = int(input())
S = list(input())

ft = fenwick_tree(N - 1)
for i in range(N - 1):
    # 広義単調増加じゃないところに1をつける
    if ord(S[i]) > ord(S[i + 1]):
        ft.add(i, 1)

string_ft = [fenwick_tree(N) for _ in range(26)]
for i, s in enumerate(S):
    string_ft[ord(s) - ord('a')].add(i, 1)

Q = int(input())
for _ in range(Q):
    query = list(input().split())
    t = int(query[0])
    if t == 1:
        i = int(query[1]) - 1
        c = query[2]
        prev = S[i]
        S[i] = c
        if i != N - 1:
            if ord(c) <= ord(S[i + 1]) and ord(prev) > ord(S[i + 1]):
                ft.add(i, -1)
            elif ord(c) > ord(S[i + 1]) and ord(prev) <= ord(S[i + 1]):
                ft.add(i, 1)
        if i != 0:
            if ord(S[i - 1]) > ord(c) and ord(S[i - 1]) <= ord(prev):
                ft.add(i - 1, 1)
            elif ord(S[i - 1]) <= ord(c) and ord(S[i - 1]) > ord(prev):
                ft.add(i - 1, -1)
        string_ft[ord(prev) - ord('a')].add(i, -1)
        string_ft[ord(c) - ord('a')].add(i, 1)

    elif t == 2:
        l = int(query[1]) - 1
        r = int(query[2]) - 1

        is_ok = True
        if ft.sum(l, r):
            is_ok = False

        left_st, right_st = S[l], S[r]
        left_num, right_num = ord(left_st) - ord('a'), ord(right_st) - ord('a')
        for num in range(left_num + 1, right_num):
            if string_ft[num].sum0(N) != string_ft[num].sum(l, r + 1):
                is_ok = False
        if is_ok:
            print("Yes")
        else:
            print("No")

    # for i in range(N - 1):
    #     print(ft.sum(i, i + 1), end=" ")
    # print("")
