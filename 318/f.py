from collections import deque

INF = 1 << 63

N = int(input())
X = list(map(int, input().split()))
L = list(map(int, input().split()))


def merge(lst, l, r):
    ret = []
    for ll, rr in lst:
        nl = max(ll, l)
        nr = min(rr, r)
        if nl < nr:
            ret.append((nl, nr))
    return ret


if N == 1:
    x, l = X[0], L[0]
    print(2 * l + 1)
    exit()

# dp[left_t][right_t]: (l,r)のリスト
dp = [[] * (N + 1) for _ in range(N + 1)]
dp[0][N] = [(-INF, INF)]
que = deque()
que.append((0, N))
while que:
    l, r = que.popleft()
    length = L[r - l - 1]  # 蛸足の長さ
    dp[l + 1][r].append(merge(dp[l][r], X[l] - length, X[l] + length))
    dp[l][r - 1].append(merge(dp[l][r], X[r] - length, X[r] + length))
