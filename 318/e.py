N = int(input())
A = list(map(lambda a: int(a) - 1, input().split()))

ans = 0
cnt = [0] * N
value = [0] * N
for i, a in enumerate(A):
    c = cnt[a]
    v = value[a]
    if c >= 1:
        ans += i * c - v - c
    cnt[a] += 1
    value[a] += i

for c in cnt:
    if c <= 2:
        continue
    ans -= c * (c - 1) * (c - 2) // 6

print(ans)
