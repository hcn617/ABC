N = int(input())
G = [[] for _ in range(N)]
for _ in range(N):
    f, s = map(int, input().split())
    G[f - 1].append(s)

for i in range(N):
    G[i].sort(reverse=True)

ans = 0
# 同じ味のアイスクリームの満足度
for i in range(N):
    if len(G[i]) >= 2:
        ans = max(ans, G[i][0] + G[i][1] // 2)

# 異なる味のアイスクリームの満足度
top = []
for i in range(N):
    if len(G[i]) >= 1:
        top.append(G[i][0])
top.sort(reverse=True)
ans = max(ans, sum(top[:2]))
