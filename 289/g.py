# monotone-minima

import sys

sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
B = list(map(int, input().split()))
C = list(map(int, input().split()))

B.sort()
Cs = sorted(C, reverse=True)
dic = dict()
for i, c in enumerate(Cs):
    dic[c] = i

ans = [-1] * M

def f(top, bottom, left, right):
    if bottom == top:
        val, idx = search(top, left, right)
        ans[top] = val
    mid = (top + bottom) // 2
    val, idx = search(mid, left, right)
    ans[mid] = val
    if top <= mid - 1:
        f(top, mid - 1, left, idx)
    if mid + 1 <= bottom:
        f(mid + 1, bottom, idx, right)


def search(i, left, right):
    ret = -1
    idx = -1
    c = Cs[i]
    for j in range(left, right + 1):
        val = (c + B[j]) * (N - j)
        if ret < val:
            ret = val
            idx = j
    return ret, idx


f(0, M - 1, 0, N - 1)
# print(ans)

for c in C:
    print(ans[dic[c]], end=" ")
