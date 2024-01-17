N = int(input())
Grid = [[False] * 101 for _ in range(101)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    for i in range(a, b):
        for j in range(c, d):
            Grid[i][j] = True
ans = 0
for i in range(101):
    for j in range(101):
        if Grid[i][j]: ans += 1
print(ans)
