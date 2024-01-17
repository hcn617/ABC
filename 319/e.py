import math

LCM = math.lcm(1, 2, 3, 4, 5, 6, 7, 8)  # 840


# aの倍数でb以上の数
def f(a, b):
    x = ((b - 1) // a + 1) * a
    return x


N, X, Y = map(int, input().split())
Bus = [list(map(int, input().split())) for _ in range(N - 1)]

ans_lst = [None] * LCM
for t in range(LCM):
    nt = t + X
    for bp, bt in Bus:
        nt = f(bp, nt) + bt
    nt += Y
    ans_lst[t] = nt

Q = int(input())
for _ in range(Q):
    q = int(input())
    p, mod = divmod(q, LCM)
    print(ans_lst[mod] + p * LCM)
