from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
ans = 1 << 60
for a in A:
    idx = bisect_left(B, a)
    dist = 1 << 60
    if idx > 0:
        dist = min(dist, a - B[idx - 1])
    if idx < M:
        dist = min(dist, B[idx] - a)
    ans = min(dist, ans)

print(ans)
