from collections import defaultdict
from heapq import heappop, heappush

N = int(input())
dic = defaultdict(int)
que = []
for _ in range(N):
    s, c = map(int, input().split())
    dic[s] = c
    heappush(que, s)

ans = 0
while que:
    s = heappop(que)
    c = dic[s]
    nc, mo = c // 2, c % 2
    if nc:
        ns = s * 2
        if ns not in dic:
            heappush(que, ns)
        dic[ns] += nc
    ans += mo

print(ans)
