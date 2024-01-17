K, G, M = map(int, input().split())

g, m = 0, 0
for _ in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        move = min(G - g, m)
        m -= move
        g += move
print(g, m)
