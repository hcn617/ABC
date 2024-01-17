from itertools import accumulate
from bisect import bisect_right

N, Q = map(int, input().split())
R = list(map(int, input().split()))

R.sort()
rui = list(accumulate(R))

for _ in range(Q):
    x = int(input())
    print(bisect_right(rui, x))
