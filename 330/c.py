import math
D=int(input())

ans = 1<<60
for x in range(0, 2_000_000):
    yy=math.isqrt(abs(D-x*x))
    for y in range(yy-10, yy+11):
        ans=min(ans, abs(x**2+y**2-D))