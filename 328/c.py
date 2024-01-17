from itertools import accumulate
from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
S = input()

ft = FenwickTree(N - 1)
for i in range(N - 1):
    if S[i] == S[i + 1]:
        ft.add(i, 1)

for _ in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())
    print(ft.sum(l, r))
