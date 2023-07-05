N = int(input())
L, R = [], []
for _ in range(N):
    a, b = map(int, input().split())
    L.append(a)
    R.append(b)
L.sort()
R.sort(reverse=True)
mid = N // 2
min_l, max_r = L[mid], R[mid]
max_l, min_r = R[mid - 1], L[mid - 1]
if N & 1:
    print(max_r - min_l + 1)
else:
    ans = (max_l + max_r) - (min_r + min_l) + 1
    print(ans)
