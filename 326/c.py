from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for li, el in enumerate(A):
    ri = bisect_left(A, el + M)
    ans = max(ans, ri - li)
print(ans)
