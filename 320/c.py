M = int(input())
S = [input() for _ in range(3)]

ans = 1 << 50
for i in range(M):
    for j in range(M):
        for k in range(M):
            if not (S[0][i] == S[1][j] == S[2][k]):
                continue
            now_ans = 0
            counter = [0] * M
            for m in [i, j, k]:
                now_ans = max(now_ans, m + counter[m] * M)
                counter[m] += 1
            ans = min(ans, now_ans)
if ans == 1 << 50:
    print(-1)
else:
    print(ans)
