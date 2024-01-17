from itertools import permutations


def move_cnt(tup):
    n = len(tup)
    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if tup[i] > tup[j]:
                result += 1
    return result


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

ans = 1000
for i_perm in permutations(range(H), H):
    for j_perm in permutations(range(W), W):
        C = [[A[ip][jp] for jp in j_perm] for ip in i_perm]
        if C == B:
            ans = min(ans, move_cnt(i_perm) + move_cnt(j_perm))
if ans == 1000:
    ans = -1
print(ans)
