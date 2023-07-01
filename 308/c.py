N = int(input())
P = []
for i in range(N):
    a, b = map(int, input().split())
    val = (1 << 70) * a // (a + b)
    P.append((val, -i))
P.sort(reverse=True)
for v, i in P:
    print(-i + 1, end=" ")
