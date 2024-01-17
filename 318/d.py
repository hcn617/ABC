from collections import deque
from itertools import combinations

N = int(input())
D = []
for i in range(N - 1):
    row = list(map(int, input().split()))
    D.append([0] * (i + 1) + row)
D.append([0] * N)
for i in range(N):
    for j in range(N):
        if i != j and D[i][j] == 0:
            D[i][j] = D[j][i]

dp = [0] * (1 << N)
que = deque()
que.append(0)
while que:
    state = que.popleft()
    P = [i for i in range(N) if (state >> i) & 1 == 0]
    if len(P) >= 2:
        for a, b in combinations(P, 2):
            nex_state = state
            nex_state |= 1 << a
            nex_state |= 1 << b
            if dp[nex_state] == 0:
                que.append(nex_state)
            dp[nex_state] = max(dp[nex_state], dp[state] + D[a][b])
print(max(dp))
