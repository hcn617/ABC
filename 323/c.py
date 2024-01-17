N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

B = [(-a, i) for i, a in enumerate(A)]
B.sort()  # # 点数の高い順

# 現状のポイントを計算する
now_point = [0]*N
for i, s in enumerate(S):
    now_point += i + 1
    for a, flag in zip(A, s):
        if flag == 'o':
            now_point[i] += a

max_point = max(now_point)
ans_lst = [0] * N
for i in range(N):
    point = now_point[i]
    if point == max_point:
        continue
    ans = 0  # 新たに問題を解いた回数
    # 点数の高い順に、解いてない問題を解いていく
    for a, j in B:
        if S[i][j] == 'x':
            point += a
            ans += 1
        if point > max_point:
            ans_lst[i] = ans
            break
for ans in ans_lst:
    print(ans)
