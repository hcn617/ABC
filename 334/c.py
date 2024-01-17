from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))

if K % 2 == 0:
    ans = 0
    for i in range(0, K, 2):
        ans += A[i + 1] - A[i]
    print(ans)
else:
    P = []
    for i in range(K // 2):
        P.append(A[i * 2 + 1] - A[i * 2])
    Q = []
    for j in reversed(range(K // 2)):
        Q.append(A[j * 2 + 2] - A[j * 2 + 1])
    rui_P = [0] + list(accumulate(P))
    rui_Q = [0] + list(accumulate(Q))
    ans = 10 ** 17
    for i in range(K // 2 + 1):
        ans = min(ans, rui_P[i] + rui_Q[K // 2 - i])
    print(ans)
