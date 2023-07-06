H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = 0
for i in range(H - 1):
    for j in range(W - 1):
        cnt = 0  # 黒マスの数
        for pi, pj in [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]:
            if S[pi][pj] == '#':
                cnt += 1
        if cnt in (1, 3):
            ans += 1
print(ans)
