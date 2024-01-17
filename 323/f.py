xa, ya, xb, yb, xc, yc = map(int, input().split())

if ya == yb == yc:
    xa, ya, xb, yb, xc, yc = ya, xa, yb, xb, yc, xc

pos = []
if xb < xc:
    pos.append((xb - 1, yb))
elif xb > xc:
    pos.append((xb + 1, yb))
if yb > yc:
    pos.append((xb, yb + 1))
elif yb < yc:
    pos.append((xb, yb - 1))

dist2 = abs(xb - xc) + abs(yb - yc)
f1 = xb != xc and yb != yc
f2 = xa == xb == xc and not (ya < yb < yc or yc < yb < ya)
if f1 or f2:
    dist2 += 2

ans = 1 << 80
for x, y in pos:
    dist1 = abs(x - xa) + abs(y - ya)
    ans = min(ans, dist1 + dist2)
print(ans)
