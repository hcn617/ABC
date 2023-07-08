from collections import deque

N, M = map(int, input().split())
p = [-1] + list(map(int, input().split()))

chs = [[] for _ in range(N)]
for i, pa in enumerate(p):
    if i == 0:
        continue
    chs[pa - 1].append(i)

power = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y += 1
    power[x] = max(power[x], y)

que = deque()
que.append(0)
seen = set()
while que:
    v = que.popleft()
    cost = power[v]
    for ch in chs[v]:
        que.append(ch)
        power[ch] = max(power[ch], cost - 1)

ans = 0
for el in power:
    if el > 0:
        ans += 1
print(ans)
